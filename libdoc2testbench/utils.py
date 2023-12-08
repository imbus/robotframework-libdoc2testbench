from re import sub

from robot.libdocpkg.robotbuilder import LibraryDoc


def replace_invalid_characters(name: str) -> str:
    return sub(r'[/."\'<>\\&,]', "_", name)


def print_stat(libdoc: LibraryDoc):  # Todo: Update to actual datatype count and enable again
    print(f"{libdoc.type.lower()}: {libdoc.name}")
    print(f"  {len(libdoc.keywords)} Interactions")
    data_types = libdoc.to_dictionary()["typedocs"]
    if data_types:
        print(f"  {len(data_types)} Data Types")
