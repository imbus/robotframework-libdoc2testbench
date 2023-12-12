from datetime import datetime, timezone
from pathlib import Path

from robot.libdocpkg.robotbuilder import LibraryDoc
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from libdoc2testbench.datatype_creator import CreatedDatatypes, DatatypeCreator
from libdoc2testbench.interaction_creator import InteractionCreator
from libdoc2testbench.pk_generator import PKGenerator
from libdoc2testbench.project_dump_model import (
    ProjectDump,
    TestElements,
    Testobjectversions,
)
from libdoc2testbench.project_dump_model.itb_project_export import (
    References,
    Subdivision,
)
from libdoc2testbench.project_dump_model.model_api import (
    create_project_details,
    create_project_dump,
    create_reference,
    create_settings,
    create_subdivision,
    create_testobjecversion,
)
from libdoc2testbench.uid_generator import TestElementType, UidGenerator
from libdoc2testbench.utils import print_stat, replace_invalid_characters


class ProjectDumpBuilder:
    def __init__(
        self,
        repository: str,
        library_root_name: str,
        resource_root_name: str,
        create_attachment_references: bool,
        created_datatypes: CreatedDatatypes,
    ) -> None:
        self.repository = repository
        self.library_root_name = library_root_name
        self.resource_root_name = resource_root_name
        self.create_attachment_references = create_attachment_references
        self.created_datatypes = created_datatypes
        self.other_library_created = False
        self.other_resource_created = False
        self.pk_generator = PKGenerator()
        self.uid_generator = UidGenerator(repository)
        self.project_dump = self.initialize_project_dump(
            version="3.0", build_number="230202/6a0c", repository=repository
        )

    def add_library_subdivision(
        self, libdoc: LibraryDoc, library_name_extension: str, resource_name_extension: str
    ):
        self.reference_pk = None
        library_name = replace_invalid_characters(libdoc.name)
        if libdoc.type == 'RESOURCE':
            resource_subdivision = self.create_resource_subdivision(
                libdoc, f"{library_name}{resource_name_extension}"
            )
            self.resource_root_subdivision.element.append(resource_subdivision)
        else:
            library_subdivision = self.create_library_subdivision(
                libdoc, f"{library_name}{library_name_extension}"
            )
            self.library_root_subdivision.element.append(library_subdivision)

    def create_library_subdivision(self, libdoc: LibraryDoc, subdivision_name: str) -> Subdivision:
        if not self.other_library_created:
            self.library_root_subdivision = create_subdivision(
                pk=self.pk_generator.get_pk(),
                name=self.library_root_name,
                description="Robot Framework Libraries",
                uid=self.uid_generator.get_uid(TestElementType.SUBDIVISION, self.library_root_name),
            )
            self.project_dump.testobjectversions.testobjectversion[0].test_elements.element.append(
                self.library_root_subdivision
            )
            self.other_library_created = True
        return self.create_library_subdivision_from_libdoc(libdoc, subdivision_name)

    def create_resource_subdivision(self, libdoc: LibraryDoc, subdivision_name: str) -> Subdivision:
        if not self.other_resource_created:
            self.resource_root_subdivision = create_subdivision(
                pk=self.pk_generator.get_pk(),
                name=self.resource_root_name,
                description="Robot Framework Resource Files",
                uid=self.uid_generator.get_uid(
                    TestElementType.SUBDIVISION, self.resource_root_name
                ),
            )
            self.project_dump.testobjectversions.testobjectversion[0].test_elements.element.append(
                self.resource_root_subdivision
            )
            self.other_resource_created = True
        if self.create_attachment_references:
            self.reference_pk = self.pk_generator.get_pk()
            attachment_name = str(Path(libdoc.source).name)
            reference = create_reference(
                pk=self.reference_pk,
                attachment_path=str(Path(libdoc.source).parent.resolve()),
                filename=attachment_name,
                attachment_pk=self.pk_generator.get_pk(),
                attachment_filename=attachment_name,
                attachment_file_pk=self.pk_generator.get_pk(),
            )
            self.project_dump.references.reference.append(reference)
        return self.create_library_subdivision_from_libdoc(libdoc, subdivision_name)

    def create_library_subdivision_from_libdoc(
        self, libdoc: LibraryDoc, subdivision_name: str
    ) -> Subdivision:
        library_subdivision = create_subdivision(
            pk=self.pk_generator.get_pk(),
            name=subdivision_name,
            uid=self.uid_generator.get_uid(TestElementType.SUBDIVISION, libdoc.name),
            html_description=f"<html><p> Import of {libdoc.name} {libdoc.version}</p>{libdoc.doc}</html>",
        )
        datatype_creator = DatatypeCreator(
            libdoc, self.pk_generator, self.uid_generator, self.created_datatypes
        )
        datatype_subdivision = datatype_creator.create_datatype_subdivision(libdoc.name)
        library_subdivision.element.append(datatype_subdivision)
        interaction_creator = InteractionCreator(
            libdoc, datatype_creator.datatypes, self.pk_generator, self.uid_generator
        )
        interaction_creator.get_interactions(libdoc.keywords, self.reference_pk)
        library_subdivision.element.extend(
            interaction_creator.get_interactions(libdoc.keywords, self.reference_pk)
        )
        num_datatypes = len(
            next(filter(lambda te: te.name == "_Datatypes", library_subdivision.element)).element
        )
        num_interactinos = len(library_subdivision.element) - 1
        print_stat(libdoc, num_interactinos, num_datatypes)
        return library_subdivision

    def write_project_dump(self, path: Path):
        context = XmlContext(class_type="attrs")
        config = SerializerConfig(
            encoding="UTF-8", pretty_print=True, ignore_default_attributes=False
        )
        serializer = XmlSerializer(config=config, context=context)
        with open(path, 'w', encoding="utf-8") as project_dump:
            project_dump.write(serializer.render(self.project_dump))

    def initialize_project_dump(
        self, version: str, build_number: str, repository: str
    ) -> ProjectDump:
        creation_time = datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S %z')
        references = References(reference=[]) if self.create_attachment_references else None
        return create_project_dump(
            version=version,
            build_number=build_number,
            repository=repository,
            details=create_project_details(
                name="RF Import",
                testobjectname="RF Import",
                created_time=creation_time,
                settings=create_settings(),
            ),
            references=references,
            testobjectversions=Testobjectversions(
                testobjectversion=[
                    create_testobjecversion(
                        pk=self.pk_generator.get_pk(),
                        id="RF Import",
                        created_time=creation_time,
                        description="Robot Framework Import",
                        testing_intelligence="false",
                        test_elements=TestElements(element=[]),
                    )
                ]
            ),
        )
