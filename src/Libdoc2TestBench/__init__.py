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

import os
import sys
import argparse
import shutil
from pathlib import Path
from zipfile import ZipFile

from .testbenchwriter import Libdoc2TestBenchWriter
from robot.libdocpkg import LibraryDocumentation
from robot.version import get_full_version as robot_version_print

__version__ = "1.0rc1"


def start_libdoc2testbench():
    """ Command line entry point for the Libdoc2TestBench module."""
    parser = argparse.ArgumentParser(
        description="""Robot Framework Libdoc Extension that generates imbus
                    TestBench Library import formats. The easiest way to run
                    Libdoc2TestBench is just using the `Libdoc2TestBench`
                    command and giving it one resource or library to generate
                    a zip-file at the current location.
                    """,
        usage=f"Libdoc2TestBench <LIBRARY> <output.zip>",
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
        '-s',
        '--specdocformat',
        default='HTML',
        choices=['HTML', 'RAW'],
        help="Specifies the documentation format used with XML and JSON spec files. `raw` means preserving the original documentation format and `html` means converting documentation to HTML. The default is `html`.",
    )
    parser.add_argument(
        '-F',
        '--docformat',
        choices=['ROBOT', 'HTML', 'TEXT', 'REST'],
        help="Specifies the source documentation format. Possible values are Robot Framework's documentation format, HTML, plain text, and reStructuredText. The default value can be specified in library source code and the initial default value is `ROBOT`.",
    )
    parser.add_argument('-n', '--name', help="Sets the name of the documented library or resource.")
    parser.add_argument(
        '-v',
        '--version',
        help="Sets the version of the documented library or resource written in the description.",
    )
    parser.add_argument(
        '--info',
        action='store_true',
        help='Writes the Libdoc2TestBench, Robot Framework and Python version to console.',
    )
    parser.add_argument(
        '-r', '--repository', help='Sets the repository id of the TestBench import. default = itba'
    )
    parser.add_argument(
        '-x', '--xml', action='store_true', help='Writes a single xml-file instead of the zipfile.'
    )
    parser.add_argument('-t', '--temp', help='Path to write the temporary files to.')
    parser.add_argument(
        '-k', '--pk', help='Defines from which number the pks are enumerated.', type=int
    )
    args = parser.parse_args()

    lib = args.library_or_resource
    outfile_path = args.outfile_path
    specdocformat = args.specdocformat
    docformat = args.docformat
    lib_name = args.name
    lib_version = args.version
    info_flag = args.info
    repo_id = args.repository
    xml_flag = args.xml
    temp_path = args.temp
    pk_start = args.pk

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
            pk_start,
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
    pk_start: int,
):
    # Init attachments_path, for handling a resource
    attachments_path = None

    # Holds the last generated primary key by the testbenchwriter.
    # This is used as part of the exit message on successful conversion.
    last_issued_pk = None

    # Check for availability of requested library or resource
    try:
        libdoc = LibraryDocumentation(lib_or_res, lib_name, lib_version, docformat)
    except:
        sys.exit(f"The requested module {lib_or_res} could not be found.")

    # For Resources: Copy it into a new created attachments directory
    #                And use the copy for writing the files instead.
    if libdoc.type == 'RESOURCE':
        # TODO: check for exisiting folder?
        # Create attachments directory
        attachments_path = Path(os.path.split(outfile_path)[0]).joinpath('attachments')
        attachments_path.mkdir(parents=True, exist_ok=True)

        # Copy resource and open it as libdoc
        shutil.copy2(libdoc.source, attachments_path)
        libdoc = LibraryDocumentation(
            attachments_path.joinpath(os.path.split(Path(libdoc.source))[1]),
            lib_name,
            lib_version,
            docformat,
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

    # Convert libdoc descriptions to html, otherwise assume RAW format
    if specdocformat == 'HTML':
        libdoc.convert_docs_to_html()

    # Set up outfile path
    outfile_path = outfile_path or libdoc.name
    if xml_flag:
        outfile_path = (
            outfile_path
            if os.path.splitext(outfile_path)[1].lower() == '.xml'
            else f"{outfile_path}.xml"
        )
    else:
        outfile_path = (
            outfile_path
            if os.path.splitext(outfile_path)[1].lower() == '.zip'
            else f"{outfile_path}.zip"
        )

    with open(project_dump_path, "w", encoding='UTF-8') as outfile:

        # The write method returns the last issued primary key.
        last_issued_pk = Libdoc2TestBenchWriter().write(libdoc, outfile, repo_id, pk_start)

        # If a file exists at the output path - get permission to overwrite.
        if Path(outfile_path).is_file():
            user_input = input(f'{outfile_path} already exists... overwrite? y/n? \n')
            if user_input.lower() not in ['y', 'yes']:
                sys.exit('Stopped execution - file was not changed.')
            os.remove(outfile_path)

        if xml_flag:
            # Put XML-file in output_path and leave attachments behind
            os.rename(project_dump_path, outfile_path)
        else:
            # Build the zip file and clean up.
            write_zip_file(outfile_path, project_dump_path, attachments_path)
            os.remove(project_dump_path)
            if attachments_path:
                shutil.rmtree(attachments_path)

    absolute_outfile_path = Path(outfile_path).resolve()
    print(
        f"Successfully written TestBench project dump to: \n{absolute_outfile_path}\nLast generated pk: {last_issued_pk}"
    )


def write_zip_file(outfile_path, project_dump_path, attachments=None):
    with ZipFile(outfile_path, 'w') as zip_file:
        zip_file.write(project_dump_path, 'project-dump.xml')

        # If there are attachments, add them to the zip-file.
        if attachments:
            zip_file.write(attachments)
            files = list(os.walk(attachments))[0][2]
            for file in files:
                zip_file.write(file, "attachments/" + file)
