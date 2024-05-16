import re
import sys
from os.path import relpath
from pathlib import Path
from typing import Dict, List, Optional, Union

from robot.libdocpkg import LibraryDocumentation
from robot.libdocpkg.robotbuilder import LibraryDoc


class LibdocGenerator:
    def __init__(
        self, doc_format: str, spec_format: str, exclude_patterns: Optional[List[str]]
    ) -> None:
        self.doc_format = doc_format
        self.spec_format = spec_format
        self.exclude_patterns = exclude_patterns
        self.excluded_paths = self._get_excluded_paths()

    def get_library_documentations(self, path_or_lib: str) -> Dict[str, LibraryDoc]:
        # library_path = Path(path_or_lib).absolute().relative_to(Path.cwd())
        library_path = Path(relpath(Path(path_or_lib), Path.cwd()))
        if self.excluded_paths.get(library_path.absolute()):
            return {}
        if library_path.is_file():
            if library_path.suffix in [".resource", ".py"]:
                return {library_path.name: self._create_libdoc(library_path)}
            return self._create_libdocs_from_import_list(library_path)
        try:
            library_documentation = self._create_libdoc(library_path)
            if len(library_documentation.keywords) == 0:
                return self._create_libdocs_from_directory_structure(library_path)
            return {library_path.name: library_documentation}
        except Exception as e:
            if library_path.is_dir():
                return self._create_libdocs_from_directory_structure(library_path)
            raise e

    def _create_libdoc(self, lib_or_res: Union[Path, str]) -> LibraryDoc:
        try:
            library_documentation = LibraryDocumentation(
                str(lib_or_res), doc_format=self.doc_format.value
            )
            if self.spec_format.value == 'HTML':
                library_documentation.convert_docs_to_html()
            return library_documentation
        except Exception:
            sys.exit(f"The requested module or path '{lib_or_res}' could not be found.")

    def _get_excluded_paths(self):
        paths = {}
        if not self.exclude_patterns:
            return paths
        for pattern in self.exclude_patterns:
            matches = Path.cwd().glob(pattern)
            for match in list(matches):
                paths[match] = True
                if match.is_dir():
                    resources = {file: True for file in match.glob('**/*.resource')}
                    py = {file: True for file in match.glob('**/*.py')}
                    paths.update(resources)
                    paths.update(py)
        return paths

    def _create_libdocs_from_directory_structure(self, directory: Path) -> Dict[str, LibraryDoc]:
        library_files = list(directory.glob('**/*.resource'))
        library_files.extend(list(directory.glob('**/*.py')))
        if not library_files:
            sys.exit("Directory doesn't contain any '*.resource' or '*.py' files.")
        return {
            file.as_posix(): self._create_libdoc(file)
            for file in library_files
            if not self.excluded_paths.get(file.absolute())
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
