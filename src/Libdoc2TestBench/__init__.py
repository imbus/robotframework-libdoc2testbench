#  Copyright 2021- imbus AG
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import argparse
import re
import shutil
import sys
from enum import Enum
from pathlib import Path
from zipfile import ZipFile

from robot.libdocpkg import LibraryDocumentation
from robot.libdocpkg.robotbuilder import LibraryDoc
from robot.running.arguments.argumentspec import ArgInfo
from robot.utils import safe_str
from robot.version import get_full_version as robot_version_print

from .testbenchwriter import Libdoc2TestBenchWriter

__version__ = "1.2b5"




def default_repr(self):
    if self.default is self.NOTSET:
        return None
    if (
        isinstance(self.default, (bool, int, float)) or self.default is None
    ):
        return f"${{{self.default}}}"
    if self.default == "":  # noqa: PLC1901
        return "${Empty}"
    if isinstance(self.default, Enum):
        return self.default.name
    return safe_str(self.default)


ArgInfo.default_repr = property(default_repr)


def start_libdoc2testbench():
    """Command line entry point for the Libdoc2TestBench module."""
    parser = argparse.ArgumentParser(
        description="""Robot Framework Libdoc Extension that generates imbus
                    TestBench Library import formats. The easiest way to run
                    Libdoc2TestBench is just using the `Libdoc2TestBench`
                    command and giving it one resource or library to generate
                    a zip-file at the current location.
                    """,
        usage="Libdoc2TestBench <LIBRARY> <output.zip>",
        prog='Libdoc2TestBench',
        epilog='Example: Libdoc2TestBench Browser My-Browser-Dump.zip',
    )
    parser.add_argument(
        "library_or_resource", help="RF library or resource", nargs='?', default=None
    )
    parser.add_argument(
        'outfile_path',
        nargs='?',
        default='',
        help="optional path to write output, default = project-dump.zip",
    )
    parser.add_argument(
        '-a',
        '--attachment',
        action='store_true',
        help='Defines if a resource file will be attached to all interactions.',
    )
    parser.add_argument(
        '-F',
        '--docformat',
        choices=['ROBOT', 'HTML', 'TEXT', 'REST'],
        help="Specifies the source documentation format. Possible values are Robot Framework's documentation format, HTML, plain text, and reStructuredText. The default value can be specified in library source code and the initial default value is `ROBOT`.",
    )
    parser.add_argument(
        '--libraryroot', help='Defines which subdivision name contains libraries.', default='RF'
    )
    parser.add_argument(
        '--libversion',
        help="Sets the version of the documented library or resource written in the description.",
    )
    parser.add_argument('-n', '--name', help="Sets the name of the documented library or resource.")
    parser.add_argument(
        '-r', '--repository', help='Sets the repository id of the TestBench import. default = itba'
    )
    parser.add_argument(
        '--resourceroot',
        help='Defines which subdivision name contains resources.',
        default='Resource',
    )
    parser.add_argument(
        '-s',
        '--specdocformat',
        default='HTML',
        choices=['HTML', 'RAW'],
        help="Specifies the documentation format used with XML and JSON spec files. `raw` means preserving the original documentation format and `html` means converting documentation to HTML. The default is `html`.",
    )
    parser.add_argument('-t', '--temp', help='Path to write the temporary files to.')
    parser.add_argument(
        '-x', '--xml', action='store_true', help='Writes a single xml-file instead of the zipfile.'
    )
    parser.add_argument(
        '--version',
        '--info',
        action='store_true',
        help='Writes the Libdoc2TestBench, Robot Framework and Python version to console.',
    )
    args = parser.parse_args()

    lib = args.library_or_resource
    outfile_path = args.outfile_path
    specdocformat = args.specdocformat
    docformat = args.docformat
    lib_name = args.name
    lib_version = args.libversion
    info_flag = args.version
    repo_id = args.repository
    xml_flag = args.xml
    temp_path = args.temp
    library_root = args.libraryroot
    resource_root = args.resourceroot
    attachment = args.attachment

    if info_flag:
        robot_version = robot_version_print()
        print(f'Libdoc2TestBench {__version__} [Robot Framework {robot_version}]')
        sys.exit()

    if not lib:
        sys.exit(
            'Libdoc2TestBench: error: the following arguments are required: library_or_resource'
        )
    else:
        create_project_dump(
            lib,
            outfile_path,
            specdocformat,
            docformat,
            lib_name,
            lib_version,
            repo_id,
            xml_flag,
            temp_path,
            library_root,
            resource_root,
            attachment,
        )


def create_project_dump(
    lib_or_res: str,
    outfile_path: str,
    specdocformat,
    docformat,
    lib_name,
    lib_version,
    repo_id,
    xml_flag,
    temp_path,
    library_root,
    resource_root,
    attachment: bool,
):
    # Init attachments_path, for handling a resource
    attachments_path = None

    # Holds the last generated primary key by the testbenchwriter.
    # This is used as part of the exit message on successful conversion.

    libraries, resources = get_libdoc_lists(
        lib_or_res, lib_name, lib_version, docformat, specdocformat
    )

    # If set, create necessary subdirectories
    if temp_path:
        temp_path = Path(temp_path)
        temp_path.mkdir(parents=True, exist_ok=True)
    # else just use the current directory
    else:
        temp_path = Path.cwd()

    project_dump_path = temp_path.joinpath('project-dump.xml')

    # Check for already existing project-dump.xml
    if project_dump_path.is_file():
        user_input = input('project-dump.xml already exists... overwrite? y/n? \n')
        if user_input.lower() not in ['y', 'yes']:
            sys.exit('Stopped execution - file was not changed.')

    if not outfile_path:
        lib_lists = libraries + resources
        outfile_path = lib_lists[0].name if len(lib_lists) == 1 else "project-dump"

    if xml_flag:
        outfile_path = (
            outfile_path
            if Path(outfile_path).suffix.lower() == ".xml"
            else f"{outfile_path}.xml"
        )
    else:
        outfile_path = (
            outfile_path
            if Path(outfile_path).suffix.lower() == '.zip'
            else f"{outfile_path}.zip"
        )

    with Path(project_dump_path).open( "w", encoding='UTF-8') as outfile:
        # The write method returns the last issued primary key.
        Libdoc2TestBenchWriter().write(
            libraries,
            resources,
            outfile,
            repo_id,
            library_root,
            resource_root,
            attachment,
        )

        # If a file exists at the output path - get permission to overwrite.
        if Path(outfile_path).is_file():
            user_input = input(f'{outfile_path} already exists... overwrite? y/n? \n')
            if user_input.lower() not in ['y', 'yes']:
                sys.exit('Stopped execution - file was not changed.')
            Path(outfile_path).unlink()

        if xml_flag:
            # Put XML-file in output_path and leave attachments behind
            Path(project_dump_path).rename(outfile_path)
        else:
            # Build the zip file and clean up.
            write_zip_file(outfile_path, project_dump_path, resources, attachment)
            Path(project_dump_path).unlink()
            if attachments_path:
                shutil.rmtree(attachments_path)

    absolute_outfile_path = Path(outfile_path).resolve()
    print(f"Successfully written TestBench project dump to: \n{absolute_outfile_path}")


def get_libdoc_lists(lib_or_res, lib_name, lib_version, docformat, specdocformat):
    resources = []
    libraries = []
    if Path(lib_or_res).exists():
        with Path(lib_or_res).open(encoding='UTF-8') as library_list:
            first_line = library_list.readline()
            if re.fullmatch(r'\*+\s*import\s?list(\s?\**)\n?', first_line, re.IGNORECASE):
                for line in library_list.read().splitlines():
                    if not line.strip().startswith('#') and len(line.strip()) != 0:
                        libdoc = create_libdoc(
                            line.strip(), lib_name, lib_version, docformat, specdocformat
                        )
                        if libdoc.type == 'RESOURCE':
                            resources.append(libdoc)
                        else:
                            libraries.append(libdoc)
                        print_stat(libdoc)
    if not (libraries or resources):
        libdoc = create_libdoc(lib_or_res, lib_name, lib_version, docformat, specdocformat)
        print_stat(libdoc)
        if libdoc.type == 'RESOURCE':
            resources.append(libdoc)
        else:
            libraries.append(libdoc)
    return libraries, resources


def print_stat(libdoc: LibraryDoc):
    print(f"{libdoc.type.lower()}: {libdoc.name}")
    print(f"  {len(libdoc.keywords)} Interactions")

    data_types = libdoc.to_dictionary()["dataTypes"]
    if data_types and data_types["enums"]:
        print(f"  {len(data_types['enums'])} Data Types")


def create_libdoc(lib_or_res, lib_name, lib_version, docformat, specdocformat) -> LibraryDoc:
    try:
        libdoc = LibraryDocumentation(lib_or_res, lib_name, lib_version, docformat)
        if specdocformat == 'HTML':
            libdoc.convert_docs_to_html()
        return libdoc
    except Exception:
        sys.exit(f"The requested module {lib_or_res} could not be found.")


def write_zip_file(outfile_path, project_dump_path, resources, attachment):
    with ZipFile(outfile_path, 'w') as zip_file:
        zip_file.write(project_dump_path, 'project-dump.xml')

        # If there are attachments, add them to the zip-file.
        if resources and attachment:
            for libdoc in resources:
                if Path(libdoc.source).exists():
                    zip_file.write(libdoc.source, "attachments/" + Path(libdoc.source).name)
