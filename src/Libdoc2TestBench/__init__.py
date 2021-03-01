from shutil import make_archive

from .testbenchwriter import Libdoc2TestBenchWriter
from robot.libdocpkg import LibraryDocumentation

__version__ = "0.0.1"

def create_project_dump(lib_or_res: str, outfile_path: str):
    libdoc = LibraryDocumentation(lib_or_res)
    with open(outfile_path, "w") as outfile:
        Libdoc2TestBenchWriter().write(libdoc, outfile)
    make_archive(outfile_path, 'zip')