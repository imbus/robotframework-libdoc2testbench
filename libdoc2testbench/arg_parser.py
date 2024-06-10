import argparse

parser = argparse.ArgumentParser(
    description="""Robot Framework Libdoc Extension that generates imbus
                    TestBench Library import formats. The easiest way to run
                    Libdoc2TestBench is just using the `Libdoc2TestBench`
                    command and giving it one resource or library to generate
                    a zip-file at the current location.
                    """,
    usage="Libdoc2TestBench <LIBRARY> <output_path>",
    prog='Libdoc2TestBench',
    epilog='Example: Libdoc2TestBench Browser Browser.zip',
)
parser.add_argument(
    "library",
    help="""Path to Robot Framework library or resource,
       to a directory containing libraries or an import list.""",
    nargs='?',
)
parser.add_argument(
    'output',
    nargs='?',
    help="""Optional argument to specify the path of the created project-dump.
      Can be a .zip or .xml file. Default = project-dump.zip""",
)
parser.add_argument(
    '-a',
    '--attachment',
    action='store_true',
    help="""Specifies whether the resource file, which has been used to generate the interactions,
      will be attached to those interactions.""",
)
parser.add_argument(
    '-F',
    '--documentation-format',
    choices=['ROBOT', 'HTML', 'TEXT', 'REST'],
    help="""Specifies the source documentation format. Possible values are Robot Framework's
      documentation format, HTML, plain text, and reStructuredText. The default value can be
        specified in the library source code, and the initial default value is ``ROBOT``.""",
)
parser.add_argument(
    '--library-root',
    help='Defines the subdivision name that contains the imported Robot Framework libraries.',
)
parser.add_argument(
    '--resource-root',
    help='Defines the subdivision name that contains the imported Robot Framework resources.',
)
parser.add_argument(
    '-r',
    '--repository',
    help='Sets the repository ID of the TestBench import. Default = iTB_RF',
)
parser.add_argument(
    '-s',
    '--specification-format',
    choices=['HTML', 'RAW'],
    help="""Specifies the documentation format used with XML and JSON spec files.
      ``RAW`` means preserving the original documentation format, and ``HTML``
        means converting documentation to ``HTML``. The default is ``HTML``.""",
)
parser.add_argument(
    '--version',
    '--info',
    action='store_true',
    help='Writes the Libdoc2TestBench, Robot Framework and Python version to console.',
)
parser.add_argument(
    '--library-name-extension',
    help='Adds an extension to the name of all Robot Framework library subdivisions in TestBench.',
)
parser.add_argument(
    '--resource-name-extension',
    help='Adds an extension to the name of all Robot Framework Resource subdivisions in TestBench.',
)
parser.add_argument(
    '--created-datatypes',
    choices=['ALL', 'ENUMS', 'NONE'],
    help="""Option to specify if all Robot Framework datatypes should be created in TestBench
      (``ALL``), only the enum types (``ENUMS``), or if no datatype should be created and
        only generic parameters are used (``NONE``). The default is ``ENUMS``.""",
)
parser.add_argument(
    '-e',
    '--excluded-paths',
    action='append',
    default=[],
    help="""Option to specify paths that will be ignored when generating the TestBench import.
      It can contain paths or glob patterns relative to the current working directory.""",
)
