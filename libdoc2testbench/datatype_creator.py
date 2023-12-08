from enum import Enum
from typing import List, Optional

from robot.libdocpkg.robotbuilder import LibraryDoc
from robot.running.arguments.argumentspec import ArgInfo
try:
    from robot.running.arguments.typeinfo import TypeInfo
except:
    from robot.running.arguments.argumentspec import TypeInfo

from libdoc2testbench.pk_generator import PKGenerator
from libdoc2testbench.project_dump_model import (
    Datatype,
    EquivalenceClasses,
)
from libdoc2testbench.project_dump_model.itb_project_export import (
    EquivalenceClass,
    Ref,
    Representative,
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

try:
    from robot.utils import NOT_SET
except ImportError:
    NOT_SET = ArgInfo.NOTSET


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
        self._ordering = -1024
        self.typed_dict_names: List = []
        self.enum_names: List = []
        self.standard_types: List = []
        self.typed_dicts: List = []
        self.default_datatype = None

    @property
    def ordering(self):
        self._ordering += 1024
        return self._ordering

    def _requires_datatype_creation(self, argument) -> bool:
        argument_kind = argument.kind
        if (
            not argument_kind
            or argument_kind == ArgInfo.POSITIONAL_ONLY_MARKER
            or argument_kind == ArgInfo.NAMED_ONLY_MARKER
            or argument_kind == NOT_SET
        ):
            return False
        return True

    def get_argument_types(self, argument_type: TypeInfo) -> List[TypeInfo]:
        types = []
        if argument_type.is_union:
            for type in argument_type.nested:
                types.extend(self.get_argument_types(type))
            return types
        else:
            return [argument_type]

    def _get_equivalence_class(self, datatype: Datatype, name: str) -> EquivalenceClass:
        eqc = next(
            filter(lambda eq: eq.name == name, datatype.equivalence_classes.equivalence_class),
            None,
        )
        if not eqc:
            eqc = create_equivalence_class(
                pk=self.pk_generator.get_pk(),
                name=name,
                ordering=self.ordering,
                default_representative_ref=Ref(pk="-1"),
                representatives=Representatives(representative=[]),
            )
            datatype.equivalence_classes.equivalence_class.append(eqc)
        return eqc

    def argument_corresponds_to_enum(self, argument: ArgInfo) -> bool:
        arg_type_names = [arg.name for arg in self.get_argument_types(argument.type)]
        intersections = list(set(arg_type_names).intersection(self.enum_names))
        if intersections:
            return True
        return False

    def argument_corresponds_to_typed_dict(self, argument: TypeInfo) -> bool:
        arg_type_names = [arg.name for arg in self.get_argument_types(argument.type)]
        intersections = list(set(arg_type_names).intersection(self.typed_dict_names))
        if intersections:
            return True
        return False

    def get_enum_type_name(self, argument_types: List[TypeInfo]) -> Optional[str]:
        enum = next(filter(lambda type: type.name in self.enum_names, argument_types), None)
        if enum:
            return str(enum.name)
        return None

    def get_typed_dict_name(self, argument_types: List[TypeInfo]) -> Optional[str]:
        typed_dict = next(
            filter(lambda type: type.name in self.typed_dict_names, argument_types), None
        )
        if typed_dict:
            return str(typed_dict.name)
        return None

    def add_enum_default_values(self) -> None:
        for keyword in self.libdoc.keywords:
            for argument in keyword.args:
                if not self._requires_datatype_creation(argument):
                    continue
                if not self.argument_corresponds_to_enum(argument):
                    continue
                arg_types = self.get_argument_types(argument.type)
                enum_type = self.get_enum_type_name(arg_types)
                arg_type_names = [arg_type.name for arg_type in arg_types]
                datatype = next(filter(lambda datatype: datatype.name == enum_type, self.enums))
                equivalence_class = self._get_equivalence_class(datatype, enum_type)
                if argument.default_repr and argument.default_repr not in [
                    "${None}",
                    '${True}',
                    '${False}',
                ]:
                    self.add_equivalence_class_members(equivalence_class, [argument.default_repr])
                arg_kind_default = self.get_arg_kind_default_value(argument.kind)
                if arg_kind_default:
                    equivalence_class = self._get_equivalence_class(datatype, enum_type)
                    self.add_equivalence_class_members(equivalence_class, [arg_kind_default])
                if argument.default_repr in ['${True}', '${False}'] or "bool" in arg_type_names:
                    equivalence_class = self._get_equivalence_class(datatype, "bool")
                    self.add_equivalence_class_members(equivalence_class, ['${True}', '${False}'])
                if argument.default_repr == "${None}" or "None" in arg_type_names:
                    equivalence_class = self._get_equivalence_class(datatype, "None")
                    self.add_equivalence_class_members(equivalence_class, ["${None}"])

    def add_typed_dict_default_values(self) -> None:
        for keyword in self.libdoc.keywords:
            for argument in keyword.args:
                if not self._requires_datatype_creation(argument):
                    continue
                if not self.argument_corresponds_to_typed_dict(argument):
                    continue
                arg_types = self.get_argument_types(argument.type)
                typed_dict_name = self.get_typed_dict_name(arg_types)
                arg_type_names = [arg_type.name for arg_type in arg_types]
                datatype = next(
                    filter(lambda datatype: datatype.name == typed_dict_name, self.typed_dicts)
                )
                equivalence_class = self._get_equivalence_class(datatype, typed_dict_name)
                if argument.default_repr and argument.default_repr not in [
                    "${None}",
                    '${True}',
                    '${False}',
                ]:
                    self.add_equivalence_class_members(equivalence_class, [argument.default_repr])
                arg_kind_default = self.get_arg_kind_default_value(argument.kind)
                if arg_kind_default:
                    equivalence_class = self._get_equivalence_class(datatype, typed_dict_name)
                    self.add_equivalence_class_members(equivalence_class, [arg_kind_default])
                if argument.default_repr in ['${True}', '${False}'] or "bool" in arg_type_names:
                    equivalence_class = self._get_equivalence_class(datatype, "bool")
                    self.add_equivalence_class_members(equivalence_class, ['${True}', '${False}'])
                if argument.default_repr == "${None}" or "None" in arg_type_names:
                    equivalence_class = self._get_equivalence_class(datatype, "None")
                    self.add_equivalence_class_members(equivalence_class, ["${None}"])

    def add_equivalence_class_members(
        self, equivalence_class: EquivalenceClass, members: List[str]
    ) -> None:
        existing_representatives = [
            repr.name for repr in self._get_ec_representatives(equivalence_class)
        ]
        for member in members:
            if member in existing_representatives:
                continue
            equivalence_class.representatives.representative.append(
                create_representative(
                    pk=self.pk_generator.get_pk(), name=str(member), ordering=self.ordering
                )
            )

    def get_standard_datatypes(self) -> List[Datatype]:
        datatypes: List[Datatype] = []
        for keyword in self.libdoc.keywords:
            for argument in keyword.args:
                if not self._requires_datatype_creation(argument):
                    continue
                if self.argument_corresponds_to_enum(
                    argument
                ) or self.argument_corresponds_to_typed_dict(argument):
                    continue
                arg_types = self.get_argument_types(argument.type)
                arg_type_names = [arg_type.name for arg_type in arg_types]
                datatype = next(filter(lambda dt: dt.name == argument.name, datatypes), None)
                if (
                    self.created_datatypes == CreatedDatatypes.ENUMS
                    or self.created_datatypes == CreatedDatatypes.NONE
                ):
                    datatype = self.default_datatype
                if not datatype:
                    datatype = create_datatype(
                        pk=self.pk_generator.get_pk(),
                        name=argument.name,
                        uid=self.uid_generator.get_uid(
                            TestElementType.DATATYPE, argument.name, self.libdoc.name
                        ),
                        equivalence_classes=EquivalenceClasses(equivalence_class=[]),
                    )
                    datatypes.append(datatype)
                equivalence_class = (
                    self._get_equivalence_class(datatype, "default_value")
                    if datatype.name == "default_value"
                    else self._get_equivalence_class(datatype, argument.name)
                )
                if argument.default_repr and argument.default_repr not in [
                    "${None}",
                    '${True}',
                    '${False}',
                ]:
                    self.add_equivalence_class_members(equivalence_class, [argument.default_repr])
                arg_kind_default = self.get_arg_kind_default_value(argument.kind)
                if arg_kind_default:
                    equivalence_class = (
                        self._get_equivalence_class(datatype, "default_value")
                        if datatype.name == "default_value"
                        else self._get_equivalence_class(datatype, argument.name)
                    )
                    self.add_equivalence_class_members(equivalence_class, [arg_kind_default])
                if argument.default_repr in ['${True}', '${False}'] or "bool" in arg_type_names:
                    equivalence_class = self._get_equivalence_class(datatype, "bool")
                    self.add_equivalence_class_members(equivalence_class, ['${True}', '${False}'])
                if argument.default_repr == "${None}" or "None" in arg_type_names:
                    equivalence_class = self._get_equivalence_class(datatype, "None")
                    self.add_equivalence_class_members(equivalence_class, ["${None}"])
        self.standard_types = datatypes
        return datatypes

    def get_arg_kind_default_value(self, argument_kind: str) -> Optional[str]:
        if argument_kind == ArgInfo.VAR_POSITIONAL:
            return "@{EMPTY}"
        if argument_kind == ArgInfo.VAR_NAMED:
            return "&{EMPTY}"
        return None

    def _get_ec_representatives(self, ec: EquivalenceClass) -> List[Representative]:
        if not ec.representatives or not ec.representatives.representative:
            return []
        return ec.representatives.representative

    def get_typed_dict_datatypes(self) -> List[Datatype]:
        typed_dicts = filter(lambda type_doc: type_doc.type == 'TypedDict', self.libdoc.type_docs)
        datatypes = []
        for typed_dict in typed_dicts:
            datatype = create_datatype(
                pk=self.pk_generator.get_pk(),
                name=typed_dict.name,
                uid=self.uid_generator.get_uid(
                    TestElementType.DATATYPE, typed_dict.name, self.libdoc.name
                ),
                # html_description=enum.doc,
                equivalence_classes=EquivalenceClasses(equivalence_class=[]),
            )
            datatypes.append(datatype)
            self.typed_dict_names.append(datatype.name)
        self.typed_dicts = datatypes
        return datatypes

    def get_enum_datatypes(self) -> List[Datatype]:
        enums = filter(lambda type_doc: type_doc.type == 'Enum', self.libdoc.type_docs)
        datatypes = []
        for enum in enums:
            eqc_ordering = self.ordering
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
                ordering=eqc_ordering,
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
                # html_description=enum.doc,
                equivalence_classes=EquivalenceClasses(equivalence_class=[enum_equivalence_class]),
            )
            datatypes.append(datatype)
            self.enum_names.append(datatype.name)
        self.enums = datatypes
        return datatypes

    def get_return_value_datatype(self) -> Datatype:
        self.return_value_datatype_pk = self.pk_generator.get_pk()
        self.return_value_default_repr = self.pk_generator.get_pk()
        return create_datatype(
            pk=self.return_value_datatype_pk,
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
                        ordering="0",
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
                                    pk=self.return_value_default_repr,
                                    name="",
                                    ordering="3072",
                                )
                            ]
                        ),
                    ),
                ]
            ),
        )

    def get_default_datatype(self) -> Datatype:
        self.default_value_datatype_pk = self.pk_generator.get_pk()
        self.default_datatype = create_datatype(
            pk=self.default_value_datatype_pk,
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
                        ordering="0",
                        representatives=Representatives(representative=[]),
                        default_representative_ref=Ref(pk="-1"),
                    )
                ]
            ),
        )
        return self.default_datatype

    def create_datatype_subdivision(self, library_name: str) -> Subdivision:
        datatype_subdivision = create_subdivision(
            pk=self.pk_generator.get_pk(),
            name="_Datatypes",
            uid=self.uid_generator.get_uid(TestElementType.SUBDIVISION, "_Datatypes", library_name),
        )
        datatype_subdivision.element.append(self.get_return_value_datatype())
        if (
            self.created_datatypes == CreatedDatatypes.NONE
            or self.created_datatypes == CreatedDatatypes.ENUMS
        ):
            datatype_subdivision.element.append(self.get_default_datatype())
        if (
            self.created_datatypes == CreatedDatatypes.ALL
            or self.created_datatypes == CreatedDatatypes.ENUMS
        ):
            datatype_subdivision.element.extend(self.get_enum_datatypes())
            self.add_enum_default_values()
        if self.created_datatypes == CreatedDatatypes.ALL:
            datatype_subdivision.element.extend(self.get_typed_dict_datatypes())
            self.add_typed_dict_default_values()
        datatype_subdivision.element.extend(self.get_standard_datatypes())
        return datatype_subdivision
