from pathlib import Path
from re import sub
from typing import List
from zipfile import ZipFile

from robot.libdocpkg.robotbuilder import LibraryDoc


def write_zip_file(
    project_dump_zip: Path,
    temp_project_dump_path: Path,
    resources: List[LibraryDoc],
    attachment: bool,
):
    with ZipFile(project_dump_zip, 'w') as zip_file:
        zip_file.write(temp_project_dump_path, 'project-dump.xml')
        if resources and attachment:
            for libdoc in resources:
                if Path(libdoc.source).exists():
                    zip_file.write(libdoc.source, "attachments/" + Path(libdoc.source).name)


def replace_invalid_characters(name: str) -> str:
    return sub(r'[/."\'<>\\&,]', "_", name)


def print_stat(libdoc: LibraryDoc):  # Todo: Update to actual datatype count and enable again
    print(f"{libdoc.type.lower()}: {libdoc.name}")
    print(f"  {len(libdoc.keywords)} Interactions")
    data_types = libdoc.to_dictionary()["typedocs"]
    if data_types:
        print(f"  {len(data_types)} Data Types")
