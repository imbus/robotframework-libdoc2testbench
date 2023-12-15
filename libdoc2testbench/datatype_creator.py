from enum import Enum
from typing import Dict, List, Optional

from robot.libdocpkg.robotbuilder import LibraryDoc
from robot.running.arguments.argumentspec import ArgInfo

from libdoc2testbench.argument_api import (
    get_arg_kind_default_value,
    get_argument_type_names,
    requires_datatype_creation,
)
from libdoc2testbench.datatype_storage import DatatypeStorage
from libdoc2testbench.pk_generator import PKGenerator
from libdoc2testbench.project_dump_model import (
    Datatype,
    EquivalenceClasses,
)
from libdoc2testbench.project_dump_model.itb_project_export import (
    EquivalenceClass,
    Ref,
    Representatives,
    Subdivision,
)
from libdoc2testbench.project_dump_model.model_api import (
    create_datatype,
    create_equivalence_class,
    create_representative,
    create_subdivision,
)
from libdoc2testbench.uid_generator import TestElementType, UidGenerator


class CreatedDatatypes(Enum):
    ALL = "ALL"
    ENUMS = "ENUMS"
    NONE = "NONE"


class DatatypeCreator:
    def __init__(
        self,
        libdoc: LibraryDoc,
        pk_generator: PKGenerator,
        uid_generator: UidGenerator,
        created_datatypes: CreatedDatatypes,
    ) -> None:
        self.libdoc = libdoc
        self.created_datatypes = created_datatypes
        self.pk_generator = pk_generator
        self.uid_generator = uid_generator
        self.datatypes = DatatypeStorage(pk_generator, uid_generator)

    @property
    def default_datatype(self):
        if not self.datatypes.get_datatype("default_value"):
            self.create_default_datatype()
        return self.datatypes.get_datatype("default_value")

    @property
    def ordering(self):
        self._ordering += 1024
        return self._ordering

    def create_datatype_subdivision(self, library_name: str) -> Subdivision:
        datatype_subdivision = create_subdivision(
            pk=self.pk_generator.get_pk(),
            name="_Datatypes",
            uid=self.uid_generator.get_uid(TestElementType.SUBDIVISION, "_Datatypes", library_name),
        )
        self.get_return_value_datatype()
        if self.created_datatypes.value in [
            CreatedDatatypes.ALL.value,
            CreatedDatatypes.ENUMS.value,
        ]:
            self.get_enum_datatypes()
        if self.created_datatypes.value == CreatedDatatypes.ALL.value:
            self.get_typed_dict_datatypes()
        self.get_remaining_datatypes()
        datatype_subdivision.element.extend(self.datatypes.get_datatypes())
        return datatype_subdivision

    def map_argument_to_datatype(self, argument: ArgInfo) -> Optional[str]:
        arg_type_names = get_argument_type_names(argument)
        for arg_type in arg_type_names:
            datatype = self.datatypes.get_datatype(arg_type)
            if datatype:
                return datatype
        datatype = self.datatypes.get_datatype(argument.name)
        if datatype:
            return datatype
        if self.created_datatypes.value == CreatedDatatypes.ALL.value:
            datatype = create_datatype(
                pk=self.pk_generator.get_pk(),
                name=argument.name,
                uid=self.uid_generator.get_uid(
                    TestElementType.DATATYPE, argument.name, self.libdoc.name
                ),
                equivalence_classes=EquivalenceClasses(equivalence_class=[]),
            )
            self.datatypes.add_datatype(argument.name, datatype)
        else:
            datatype = self.default_datatype
        return datatype

    def get_remaining_datatypes(self) -> None:
        for keyword in self.libdoc.keywords:
            for arg in keyword.args:
                if not requires_datatype_creation(arg):
                    continue
                datatype = self.map_argument_to_datatype(arg)
                arg_type_names = get_argument_type_names(arg)
                arg_kind_default = get_arg_kind_default_value(arg.kind)
                equivalence_class = self.datatypes.get_equivalence_class(
                    datatype.name, datatype.name
                )
                if arg.default_repr and arg.default_repr not in ["${None}", '${True}', '${False}']:
                    self.datatypes.add_equivalence_class_members(
                        datatype.name, equivalence_class.name, [arg.default_repr]
                    )
                if arg_kind_default:
                    self.datatypes.add_equivalence_class_members(
                        datatype.name, datatype.name, [arg_kind_default]
                    )
                if arg.default_repr in ['${True}', '${False}'] or "bool" in arg_type_names:
                    self.datatypes.add_equivalence_class_members(
                        datatype.name, "bool", ['${True}', '${False}']
                    )
                if arg.default_repr == "${None}" or "None" in arg_type_names:
                    self.datatypes.add_equivalence_class_members(datatype.name, "None", ["${None}"])

    def get_enum_datatypes(self) -> List[Datatype]:
        enums = filter(lambda type_doc: type_doc.type == 'Enum', self.libdoc.type_docs)
        for enum in enums:
            self._ordering = 0
            representatives = Representatives(
                representative=[
                    create_representative(
                        pk=self.pk_generator.get_pk(),
                        name=member.name,
                        ordering=str(self.ordering),
                    )
                    for member in enum.members
                ]
            )
            enum_equivalence_class = EquivalenceClass(
                pk=self.pk_generator.get_pk(),
                ordering="1024",
                name=enum.name,
                description=enum.name,
                representatives=representatives,
                default_representative_ref=Ref(pk=representatives.representative[0].pk),
            )
            datatype = create_datatype(
                pk=self.pk_generator.get_pk(),
                name=enum.name,
                uid=self.uid_generator.get_uid(
                    TestElementType.DATATYPE, enum.name, self.libdoc.name
                ),
                html_description=f"<html>{enum.doc}</html>",
                equivalence_classes=EquivalenceClasses(equivalence_class=[enum_equivalence_class]),
            )
            self.datatypes.add_datatype(enum.name, datatype)

    def get_typed_dict_datatypes(self) -> List[Datatype]:
        typed_dicts = filter(lambda type_doc: type_doc.type == 'TypedDict', self.libdoc.type_docs)
        self.typed_dict_dicts: Dict[str, Datatype] = {}
        for typed_dict in typed_dicts:
            datatype = create_datatype(
                pk=self.pk_generator.get_pk(),
                name=typed_dict.name,
                uid=self.uid_generator.get_uid(
                    TestElementType.DATATYPE, typed_dict.name, self.libdoc.name
                ),
                html_description=f"<html>{typed_dict.doc}</html>",
                equivalence_classes=EquivalenceClasses(equivalence_class=[]),
            )
            self.datatypes.add_datatype(typed_dict.name, datatype)

    def get_return_value_datatype(self) -> Datatype:
        datatype = create_datatype(
            pk=self.pk_generator.get_pk(),
            name="assigned_variable",
            uid=self.uid_generator.get_uid(
                TestElementType.DATATYPE, "assigned_variable", self.libdoc.name
            ),
            equivalence_classes=EquivalenceClasses(
                equivalence_class=[
                    create_equivalence_class(
                        pk=self.pk_generator.get_pk(),
                        name="assigned_variable",
                        description=r"regex:(?<robotVariableSyntax>\$\{.*})",
                        ordering="1024",
                        default_representative_ref=Ref(pk="-1"),
                        representatives=Representatives(
                            representative=[
                                create_representative(
                                    pk=self.pk_generator.get_pk(),
                                    name="${return_value}",
                                    ordering="1024",
                                )
                            ]
                        ),
                    ),
                    create_equivalence_class(
                        pk=self.pk_generator.get_pk(),
                        name="no_assignment",
                        description="regex:^$",
                        ordering="2048",
                        default_representative_ref=Ref(pk="-1"),
                        representatives=Representatives(
                            representative=[
                                create_representative(
                                    pk=self.pk_generator.get_pk(),
                                    name="",
                                    ordering="1024",
                                )
                            ]
                        ),
                    ),
                ]
            ),
        )
        self.datatypes.add_datatype("assigned_variable", datatype)

    def create_default_datatype(self) -> Datatype:
        datatype = create_datatype(
            pk=self.pk_generator.get_pk(),
            name="default_value",
            uid=self.uid_generator.get_uid(
                TestElementType.DATATYPE, "default_value", self.libdoc.name
            ),
            equivalence_classes=EquivalenceClasses(
                equivalence_class=[
                    create_equivalence_class(
                        pk=self.pk_generator.get_pk(),
                        name="default_value",
                        description="",
                        ordering="1024",
                        representatives=Representatives(representative=[]),
                        default_representative_ref=Ref(pk="-1"),
                    )
                ]
            ),
        )
        self.datatypes.add_datatype("default_value", datatype)
