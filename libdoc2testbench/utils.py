from re import sub

from robot.libdocpkg.robotbuilder import LibraryDoc


def replace_invalid_characters(name: str) -> str:
    return sub(r'[/."\'<>\\&,]', "_", name)


def print_stat(libdoc: LibraryDoc, num_interactinos: int, num_datatypes: int) -> None:
    print(f"{libdoc.type.lower()}: {libdoc.name}")
    print(f"  {num_interactinos} Interactions")
    data_types = libdoc.to_dictionary()["typedocs"]
    if data_types:
        print(f"  {num_datatypes} Data Types")
