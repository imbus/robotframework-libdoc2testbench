import re
import sys
from os.path import commonpath
from pathlib import Path
from typing import Dict, Union

from robot.libdocpkg import LibraryDocumentation
from robot.libdocpkg.robotbuilder import LibraryDoc


class LibdocGenerator:
    def __init__(self, lib_name: str, lib_version: str, doc_format: str, spec_format: str) -> None:
        self.lib_name = lib_name
        self.lib_version = lib_version
        self.doc_format = doc_format
        self.spec_format = spec_format

    def get_library_documentations(self, path_or_lib: str) -> Dict[str, LibraryDoc]:
        if not Path(path_or_lib).exists():
            return {path_or_lib: self._create_libdoc(path_or_lib)}
        library_path = Path(path_or_lib)
        if library_path.suffix in [".resource", ".py"]:
            return {library_path.name: self._create_libdoc(library_path)}
        if library_path.is_dir():
            libdocs = self._create_libdocs_from_directory_structure(library_path)
        else:
            libdocs = self._create_libdocs_from_import_list(library_path)
        return libdocs

    def _create_libdoc(self, lib_or_res: Union[Path, str]) -> LibraryDoc:
        try:
            library_documentation = LibraryDocumentation(
                str(lib_or_res), self.lib_name, self.lib_version, self.doc_format
            )
            if self.spec_format == 'HTML':
                library_documentation.convert_docs_to_html()
            return library_documentation
        except Exception:
            sys.exit(f"The requested module {lib_or_res} could not be found.")

    def _create_libdocs_from_directory_structure(self, directory: Path) -> Dict[str, LibraryDoc]:
        library_files = list(directory.glob('**/*.resource'))
        library_files.extend(list(directory.glob('**/*.py')))
        library_posix_paths = [file.as_posix() for file in library_files]
        common_path = Path(commonpath(library_posix_paths)).as_posix()
        return {
            str(file).replace(f"{common_path}/", ""): self._create_libdoc(file)
            for file in library_posix_paths
        }

    def _create_libdocs_from_import_list(self, import_list: Path) -> Dict[str, LibraryDoc]:
        library_documentations = {}
        with Path(import_list).open(encoding='UTF-8') as library_list:
            first_line = library_list.readline()
            if not re.fullmatch(r'\*+\s*import\s?list(\s?\**)\n?', first_line, re.IGNORECASE):
                sys.exit(
                    f"Import list {import_list} should contain the following header:"
                    f" *** Import List ***"
                )
            for line in library_list.read().splitlines():
                import_statement = line.strip()
                if not import_statement.startswith('#') and len(import_statement) != 0:
                    library_documentations.update(self.get_library_documentations(import_statement))
        return library_documentations
