import re
import sys
from pathlib import Path
from typing import List

from robot.libdocpkg import LibraryDocumentation
from robot.libdocpkg.robotbuilder import LibraryDoc


def create_libdoc(
    lib_or_res, lib_name: str, lib_version: str, doc_format: str, spec_format: str
) -> LibraryDoc:
    try:
        library_documentation = LibraryDocumentation(lib_or_res, lib_name, lib_version, doc_format)
        if spec_format == 'HTML':
            library_documentation.convert_docs_to_html()
        return library_documentation
    except Exception:
        sys.exit(f"The requested module {lib_or_res} could not be found.")


def create_libdocs_from_import_list(
    import_list: Path, lib_name: str, lib_version: str, doc_format: str, spec_format: str
) -> List[LibraryDoc]:
    library_documentations = []
    with Path(import_list).open(encoding='UTF-8') as library_list:
        first_line = library_list.readline()
        if not re.fullmatch(r'\*+\s*import\s?list(\s?\**)\n?', first_line, re.IGNORECASE):
            sys.exit(
                f"Import list {import_list} should contain the following header: *** Import List ***"
            )
        for line in library_list.read().splitlines():
            if not line.strip().startswith('#') and len(line.strip()) != 0:
                library_documentation = create_libdoc(
                    line.strip(), lib_name, lib_version, doc_format, spec_format
                )
                library_documentations.append(library_documentation)
    return library_documentations


def get_library_documentations(
    library_or_path: str,
    library_name: str,
    library_version: str,
    documentation_format: str,
    spec_format: str,
) -> List[LibraryDoc]:
    if not Path(library_or_path).exists() or Path(library_or_path).suffix == ".resource":
        libdocs = [
            create_libdoc(
                library_or_path, library_name, library_version, documentation_format, spec_format
            )
        ]
    else:
        libdocs = create_libdocs_from_import_list(
            Path(library_or_path), library_name, library_version, documentation_format, spec_format
        )
    return libdocs
