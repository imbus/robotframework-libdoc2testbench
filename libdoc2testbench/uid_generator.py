from enum import Enum
from hashlib import sha1
from re import sub
from typing import ClassVar


class TestElementType(Enum):
    SUBDIVISION = "subdivision"
    INTERACTION = "interaction"
    DATATYPE = "datatype"


class UidGenerator:
    type_abbrev: ClassVar = {
        TestElementType.SUBDIVISION: "SD",
        TestElementType.INTERACTION: "IA",
        TestElementType.DATATYPE: "DT",
    }

    def __init__(self, repository) -> None:
        self.repository = repository

    def get_uid(
        self,
        test_element_type: TestElementType,
        test_element_name: str,
        lib_name: str = "",
    ) -> str:
        # UIDs format:
        # Prefix: RepositoryID-ElementTypeAbbreviation-Root
        # Root: first 10 characters of sha1Hash of LibraryName.ElementName
        test_element_name = sub(r'[_ ]', "", test_element_name)
        test_element_name = test_element_name.lower()
        root_hash = sha1(f"{lib_name}.{test_element_name}".encode()).hexdigest()[:10]
        return f"{self.repository}-{self.type_abbrev.get(test_element_type)}-{root_hash}"
