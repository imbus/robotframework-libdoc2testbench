import sys

import robot

from libdoc2testbench import __version__
from libdoc2testbench.arg_parser import parser
from libdoc2testbench.testbench_import_generator import TestBenchImportGenerator


def run():
    args = parser.parse_args()
    version_info = args.version
    if version_info:
        print(
            f"Libdoc2TestBench {__version__} [Robot Framework {robot.version.get_full_version()}]"
        )
        sys.exit()
    library = args.library_or_resource
    if not library:
        sys.exit("Libdoc2TestBench error: Missing required argument 'library_or_resource'")
    TestBenchImportGenerator(args).create_project_dump()


if __name__ == "__main__":
    run()
