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
    args = parser.parse_args()

    lib = args.library_or_resource
    outfile_path = args.outfile_path
    specdocformat = args.specdocformat
    docformat = args.docformat
    lib_name = args.name
    lib_version = args.version
    info = args.info

    if info:
        robot_version = robot_version_print()
        print(f'Libdoc2TestBench {__version__} [Robot Framework {robot_version}]')
        sys.exit()

    if not lib:
        sys.exit(
            'Libdoc2TestBench: error: the following arguments are required: library_or_resource'
        )
    else:
        create_project_dump(lib, outfile_path, specdocformat, docformat, lib_name, lib_version)


def create_project_dump(
    lib_or_res: str, outfile_path: str, specdocformat, docformat, lib_name, lib_version
):
    # Check for already existing project-dump.xml
    if Path('project-dump.xml').is_file():
        user_input = input('project-dump.xml already exists... overwrite? y/n? \n')
        if user_input.lower() not in ['y', 'yes']:
            print('stopped execution')
            sys.exit()

    # Check for availability of requested library or resource
    try:
        libdoc = LibraryDocumentation(lib_or_res, lib_name, lib_version, docformat)
    except:
        sys.exit(f"The requested module {lib_or_res} could not be found.")
    outfile_path = outfile_path or libdoc.name
    outfile_path = (
        outfile_path if os.path.splitext(outfile_path)[1] == '.zip' else f"{outfile_path}.zip"
    )
    if specdocformat == 'HTML':
        libdoc.convert_docs_to_html()
    with open('project-dump.xml', "w", encoding='UTF-8') as outfile:
        Libdoc2TestBenchWriter().write(libdoc, outfile)
    write_zip_file(outfile_path)
    os.remove('project-dump.xml')
    absolute_outfile_path = Path(outfile_path).resolve()
    print(f"Successfully written TestBench project dump to: \n{absolute_outfile_path}")


def write_zip_file(outfile_path):
    with ZipFile(outfile_path, 'w') as zip_file:
        zip_file.write('project-dump.xml', 'project-dump.xml')
