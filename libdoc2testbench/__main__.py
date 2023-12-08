import sys

import robot

from libdoc2testbench import __version__
from libdoc2testbench.arg_parser import parser
from libdoc2testbench.import_generator import create_project_dump


def run():
    args = parser.parse_args()
    library = args.library_or_resource
    version_info = args.version
    if version_info:
        print(
            f'Libdoc2TestBench {__version__} [Robot Framework {robot.version.get_full_version()}]'
        )
        sys.exit()
    if not library:
        sys.exit(
            'Libdoc2TestBench: error: The following arguments are required: library_or_resource'
        )
    create_project_dump(args)


if __name__ == "__main__":
    run()
