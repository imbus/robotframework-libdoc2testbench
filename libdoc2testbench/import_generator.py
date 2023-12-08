import sys
from argparse import Namespace
from pathlib import Path

from libdoc2testbench.datatype_creator import CreatedDatatypes
from libdoc2testbench.libdoc_generation import get_library_documentations
from libdoc2testbench.project_dump_builder import ProjectDumpBuilder
from libdoc2testbench.utils import check_for_existing_file, write_zip_file


def create_project_dump(cli_args: Namespace) -> None:
    libdocs = get_library_documentations(
        cli_args.library_or_resource,
        cli_args.name,
        cli_args.libversion,
        cli_args.docformat,
        cli_args.specdocformat,
    )

    project_dump_path = cli_args.outfile_path
    if not project_dump_path:
        project_dump_path = f"{libdocs[0].name}.zip" if len(libdocs) == 1 else "project-dump.zip"
    elif Path(cli_args.outfile_path).suffix.lower() not in [".zip", ".xml"]:
        sys.exit("outfile_path must end with '.xml' or '.zip'")

    project_dump = ProjectDumpBuilder(
        cli_args.repository,
        cli_args.libraryroot,
        cli_args.resourceroot,
        cli_args.attachment,
        CreatedDatatypes[cli_args.created_datatypes],
    )
    for libdoc in libdocs:
        project_dump.add_library_subdivision(
            libdoc, cli_args.library_name_extension, cli_args.resource_name_extension
        )
    temp_path = Path.cwd() / Path("project-dump.xml")
    project_dump.write_project_dump(temp_path)

    check_for_existing_file(Path(project_dump_path))
    if Path(project_dump_path).suffix.lower() == ".xml":
        Path(temp_path).rename(project_dump_path)
    else:
        write_zip_file(
            Path(project_dump_path),
            temp_path,
            list(filter(lambda libdoc: libdoc.type == "RESOURCE", libdocs)),
            cli_args.attachment,
        )
        temp_path.unlink()
    print(f"Successfully written TestBench project dump to: \n{Path(project_dump_path).resolve()}")
