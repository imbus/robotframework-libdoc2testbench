import argparse

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
parser.add_argument("library_or_resource", help="RF library or resource", nargs='?', default=None)
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
parser.add_argument('--libname', help="Sets the name of the documented library or resource.")
parser.add_argument(
    '-r',
    '--repository',
    help='Sets the repository id of the TestBench import. default = iTB_RF',
    default='iTB_RF',
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

parser.add_argument(
    '--version',
    '--info',
    action='store_true',
    help='Writes the Libdoc2TestBench, Robot Framework and Python version to console.',
)
parser.add_argument(
    '--library_name_extension',
    help='Adds an extension to the name of an Robot Framework Library Subdivision in TestBench.',
    default=' [Robot-Library]',
)
parser.add_argument(
    '--resource_name_extension',
    help='Adds an extension to the name of an Robot Framework Resource Subdivision in TestBench.',
    default=' [Robot-Resource]',
)
parser.add_argument(
    '--created_datatypes',
    default='ALL',
    choices=['ALL', 'ENUMS', 'NONE'],
    help="Option to specify if all Robot Framework datatypes should be created in TestBench (`ALL`), only the enum types (`ENUMS`) or if no datatype should be created and only generic parameters are used (`NONE`). The default is `ALL`.",
)
