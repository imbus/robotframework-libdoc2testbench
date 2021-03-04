import os
from pathlib import Path
from zipfile import ZipFile
from .testbenchwriter import Libdoc2TestBenchWriter
from robot.libdocpkg import LibraryDocumentation
from robot.utils.robotio import file_writer

__version__ = "0.0.1"

def create_project_dump(lib_or_res: str, outfile_path: str):
    libdoc = LibraryDocumentation(lib_or_res)
    libdoc.convert_docs_to_html()
    if Path('project-dump.xml').is_file():
        user_input = input('project-dump.xml already exists... overwrite? y/n? \n')
        if user_input.lower() in ['y', 'yes']:
            with open('project-dump.xml', "w", encoding='UTF-8') as outfile:
                Libdoc2TestBenchWriter().write(libdoc, outfile)
            write_zip_file(outfile_path)
            os.remove('project-dump.xml')
            print("Successfully written zip file")
        else:
            print('stopped execution')

def write_zip_file(outfile_path):
    with ZipFile(outfile_path, 'w') as zip_file:
        zip_file.write('project-dump.xml', 'project-dump.xml')