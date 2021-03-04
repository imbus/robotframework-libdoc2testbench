import sys
import argparse
from os import path
from Libdoc2TestBench import create_project_dump

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Robot Framework Libdoc Extension that generates imbus TestBench Library import formats.",
        usage=f"Libdoc2TestBench <LIBRARY> -o <output.zip>",
        prog='Libdoc2TestBench')
    parser.add_argument("library_or_resource",
                        help="RF library or resource", default='project-dump.zip')
    parser.add_argument('-o', '--outfile_path', nargs='?',
                        help="path to write output, default=project-dump.zip")
    args = parser.parse_args()

    lib = args.library_or_resource
    outfile_path = args.outfile_path

    create_project_dump(lib, outfile_path)
