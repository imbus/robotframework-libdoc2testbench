from dataclasses import dataclass
from enum import Enum
import sys
from argparse import Namespace
from typing import Optional


if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

from pathlib import Path


class CreatedDatatypes(Enum):
    ALL = "ALL"
    ENUMS = "ENUMS"
    NONE = "NONE"


class DocumentationFormat(Enum):
    ROBOT = "ROBOT"
    HTML = "HTML"
    TEXT = "TEXT"
    REST = "REST"


class SpecificationFormat(Enum):
    RAW = "RAW"
    HTML = "HTML"


@dataclass
class Configuration:
    attachment: bool
    documentation_format: DocumentationFormat
    library_root: str
    resource_root: str
    library_version: Optional[str]
    library_name: Optional[str]
    repository_id: str
    specification_format: SpecificationFormat
    library_name_extension: str
    resource_name_extension: str
    created_datatypes: CreatedDatatypes

    @classmethod
    def from_cli_args(cls, cli_args: Namespace):
        with open(Path.cwd() / "pyproject.toml", "rb") as f:
            toml_dict = tomllib.load(f)
        toml_config = toml_dict.get("tool", {}).get("libdoc2testbench",{})

        attachment_config = cli_args.attachment or toml_config.get("attachment")
        docFormat = cli_args.docformat or toml_config.get("documentation_format")
        libraryRoot = cli_args.libraryroot or toml_config.get("library_root")
        resourceRoot = cli_args.resourceroot or toml_config.get("resource_root")
        library_version = cli_args.libversion or toml_config.get("library_version")
        library_name = cli_args.libname or toml_config.get("library_name")
        repositoryId = cli_args.repository or toml_config.get("repository_id")
        specFormat = cli_args.specdocformat or toml_config.get("specification_format")
        libraryNameExtension = cli_args.library_name_extension or toml_config.get("library_name_extension")
        resourceNameExtension = cli_args.resource_name_extension or toml_config.get("resource_name_extension")
        createdDatatypes = cli_args.created_datatypes or toml_config.get("created_datatypes")
        return cls(
            attachment = attachment_config or False,
            documentation_format = DocumentationFormat[docFormat] if docFormat else DocumentationFormat.ROBOT,
            library_root = libraryRoot or "RF",
            resource_root = resourceRoot or "Resource",
            library_version = library_version,
            library_name = library_name,
            repository_id = repositoryId or "iTB_RF",
            specification_format = SpecificationFormat[specFormat] if specFormat else SpecificationFormat.HTML,
            resource_name_extension = resourceNameExtension or " [Robot-Resource]",
            library_name_extension = libraryNameExtension or " [Robot-Library]",
            created_datatypes = CreatedDatatypes[createdDatatypes] if createdDatatypes else CreatedDatatypes.ENUMS
        )

        # self.library_or_resource: str = cli_args.library_or_resource
        # self.output_path: str = cli_args.outfile_path



