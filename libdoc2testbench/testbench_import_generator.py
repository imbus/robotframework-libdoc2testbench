import sys
from argparse import Namespace
from pathlib import Path

from libdoc2testbench.datatype_creator import CreatedDatatypes
from libdoc2testbench.libdoc_generation import get_library_documentations
from libdoc2testbench.project_dump_builder import ProjectDumpBuilder
from libdoc2testbench.utils import write_zip_file


class TestBenchImportGenerator:
    def __init__(self, cli_args: Namespace) -> None:
        self.library_or_resource: str = cli_args.library_or_resource
        self.output_path: str = cli_args.outfile_path
        self.attachment: bool = cli_args.attachment
        self.library_root: str = cli_args.libraryroot
        self.resource_root: str = cli_args.resourceroot
        self.doc_format: str = cli_args.specdocformat
        self.spec_format: str = cli_args.specdocformat
        self.lib_name: str = cli_args.libname
        self.lib_version: str = cli_args.libversion
        self.repository: str = cli_args.repository
        self.lib_name_ext: str = cli_args.library_name_extension
        self.res_name_ext: str = cli_args.resource_name_extension
        self.created_datatypes: CreatedDatatypes = CreatedDatatypes[cli_args.created_datatypes]

    def create_project_dump(self) -> None:
        self.libdocs = get_library_documentations(
            self.library_or_resource,
            self.lib_name,
            self.lib_version,
            self.doc_format,
            self.spec_format,
        )
        project_dump_path = self.get_project_dump_path()
        self.check_for_existing_dump(project_dump_path)
        self.write_temp_dump()
        self.save_project_dump(project_dump_path)

    def get_project_dump_path(self) -> str:
        project_dump_path = self.output_path
        if not project_dump_path:
            project_dump_path = (
                f"{self.libdocs[0].name}.zip" if len(self.libdocs) == 1 else "project-dump.zip"
            )
        elif Path(self.output_path).suffix.lower() not in [".zip", ".xml"]:
            sys.exit("Output path must end with '.xml' or '.zip'")
        return Path(project_dump_path)

    def write_temp_dump(self) -> None:
        project_dump = ProjectDumpBuilder(
            self.repository,
            self.library_root,
            self.resource_root,
            self.attachment,
            self.created_datatypes,
        )
        for libdoc in self.libdocs:
            project_dump.add_library_subdivision(libdoc, self.lib_name_ext, self.res_name_ext)
        self.temp_path = Path.cwd() / Path("project-dump.xml")
        project_dump.write_project_dump(self.temp_path)

    def check_for_existing_dump(self, dump: Path) -> None:
        if dump.is_file():
            user_input = input(f"'{dump}' already exists... overwrite? y/n? \n")
            if user_input.lower() not in ['y', 'yes']:
                sys.exit('Stopped execution - file was not changed.')
            Path(dump).unlink()

    def save_project_dump(self, dump_path: Path):
        if dump_path.suffix.lower() == ".xml":
            Path(self.temp_path).rename(str(dump_path))
        else:
            write_zip_file(
                dump_path,
                self.temp_path,
                list(filter(lambda libdoc: libdoc.type == "RESOURCE", self.libdocs)),
                self.attachment,
            )
            self.temp_path.unlink()
        print(f"Successfully written TestBench project dump to: \n{Path(dump_path).resolve()}")
