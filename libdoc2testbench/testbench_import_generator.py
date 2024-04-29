import sys
from pathlib import Path
from zipfile import ZipFile

from libdoc2testbench.configuration import Configuration
from libdoc2testbench.libdoc_generation import LibdocGenerator
from libdoc2testbench.project_dump_builder import ProjectDumpBuilder


class TestBenchImportGenerator:
    def __init__(self, config: Configuration) -> None:
        self.config = config

    def create_project_dump(self) -> None:
        libdoc_genertor = LibdocGenerator(
            self.config.library_name,
            self.config.library_version,
            self.config.documentation_format,
            self.config.specification_format,
        )
        self.libdocs = libdoc_genertor.get_library_documentations(self.config.input_path)
        project_dump_path = self.get_project_dump_path()
        self.check_for_existing_dump(project_dump_path)
        self.write_temp_dump()
        self.save_project_dump(project_dump_path)

    def get_project_dump_path(self) -> Path:
        project_dump_path = self.config.output_path
        if not project_dump_path:
            project_dump_path = (
                f"{next(iter(self.libdocs.items()))[1].name}.zip"
                if len(self.libdocs) == 1
                else "project-dump.zip"
            )
        elif Path(self.config.output_path).suffix.lower() not in [".zip", ".xml"]:
            sys.exit("Output path must end with '.xml' or '.zip'")
        return Path(project_dump_path)

    def write_temp_dump(self) -> None:
        project_dump = ProjectDumpBuilder(
            self.config.repository_id,
            self.config.library_root,
            self.config.resource_root,
            self.config.attachment,
            self.config.created_datatypes,
        )
        for path, libdoc in self.libdocs.items():
            project_dump.add_library_subdivision(
                libdoc,
                path,
                self.config.library_name_extension,
                self.config.resource_name_extension,
            )
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
            self.write_zip_dump(dump_path)
            self.temp_path.unlink()
        print(f"Successfully written TestBench project dump to: \n{Path(dump_path).resolve()}")

    def write_zip_dump(self, project_dump_zip: Path):
        # resources = list(filter(lambda libdoc: libdoc.type == "RESOURCE", self.libdocs.values()))
        resources = {
            path: libdoc for path, libdoc in self.libdocs.items() if libdoc.type == "RESOURCE"
        }
        with ZipFile(project_dump_zip, 'w') as zip_file:
            zip_file.write(self.temp_path, 'project-dump.xml')
            if resources and self.config.attachment:
                for resource_path, libdoc in resources.items():
                    if Path(libdoc.source).exists():
                        zip_file.write(
                            libdoc.source, "attachments/" + Path(resource_path).as_posix()
                        )
