#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
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

__version__ = "0.0.1"


def run():
    """ Command line entry point for the Libdic2TestBench module."""
    parser = argparse.ArgumentParser(
        description="Robot Framework Libdoc Extension that generates imbus \
            TestBench Library import formats. \n The easiest way to run \
            Libdoc2TestBench is just using the `Libdoc2TestBench` command  \
            and giving it one resource or library to generate a zip-file at \
            the current location. However, this module can also be executed \
            via python -m Libdoc2TestBench <LIBRARY>.",
        usage=f"Libdoc2TestBench <LIBRARY> <output.zip>",
        prog='Libdoc2TestBench',
        epilog='Example: python -m Libdoc2TestBench Browser My-Browser-Dump.zip')
    parser.add_argument("library_or_resource",
                        help="RF library or resource")
    parser.add_argument('outfile_path', nargs='?', default='project-dump.zip',
                        help="optional path to write output, default = project-dump.zip")
    parser.add_argument('-s', '--specdocformat', default= 'RAW', choices=['HTML', 'RAW'],
                        help="Specifies the documentation format used with XML and JSON spec files. `raw` means preserving the original documentation format and `html` means converting documentation to HTML. The default is `html`.")
    parser.add_argument('-F', '--docformat', choices=['ROBOT', 'HTML', 'TEXT', 'REST'],
                        help="Specifies the source documentation format. Possible values are Robot Framework's documentation format, HTML, plain text, and reStructuredText. The default value can be specified in library source code and the initial default value is `ROBOT`.")
    parser.add_argument(
        '-n', '--name', help="Sets the name of the documented library or resource.")
    parser.add_argument(
        '-v', '--version', help="Sets the version of the documented library or resource written in the description.")
    args = parser.parse_args()

    lib = args.library_or_resource
    outfile_path = args.outfile_path
    specdocformat = args.specdocformat
    docformat = args.docformat
    lib_name = args.name
    lib_version = args.version

    create_project_dump(lib, outfile_path, specdocformat,
                        docformat, lib_name, lib_version)


def create_project_dump(lib_or_res: str, outfile_path: str, specdocformat, docformat, lib_name, lib_version):
    # Check for already existing project-dump.xml
    if Path('project-dump.xml').is_file():
        user_input = input(
            'project-dump.xml already exists... overwrite? y/n? \n')
        if user_input.lower() not in ['y', 'yes']:
            print('stopped execution')
            sys.exit()

    libdoc = LibraryDocumentation(lib_or_res, lib_name, lib_version, docformat)
    libdoc.convert_docs_to_html() #TODO: -s param
    with open('project-dump.xml', "w", encoding='UTF-8') as outfile:
        Libdoc2TestBenchWriter().write(libdoc, outfile)
    write_zip_file(outfile_path)
    os.remove('project-dump.xml')
    print(f"Successfully written zip file to {outfile_path}")


def write_zip_file(outfile_path):
    with ZipFile(outfile_path, 'w') as zip_file:
        zip_file.write('project-dump.xml', 'project-dump.xml')
