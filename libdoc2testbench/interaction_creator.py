from typing import List, Optional

try:
    from robot.running.arguments.typeinfo import TypeInfo
except ImportError:
    try:
        from robot.running.arguments.argumentspec import TypeInfo
    except ImportError:
        from robot.running.arguments.argumentspec import ArgInfo as TypeInfo
from robot.libdocpkg.model import KeywordDoc
from robot.libdocpkg.robotbuilder import LibraryDoc
from robot.running.arguments.argumentspec import ArgInfo

from libdoc2testbench.datatype_storage import DatatypeStorage
from libdoc2testbench.pk_generator import PKGenerator
from libdoc2testbench.project_dump_model import (
    Interaction,
    Parameter,
    Parameters,
    Ref,
    References,
)
from libdoc2testbench.project_dump_model.itb_project_export import (
    DefaultValue,
    DefaultValueType,
    DefinitionType,
    UseType,
)
from libdoc2testbench.project_dump_model.model_api import create_interaction
from libdoc2testbench.uid_generator import TestElementType, UidGenerator

try:
    from robot.utils import NOT_SET
except ImportError:
    NOT_SET = ArgInfo.NOTSET


class InteractionCreator:
    def __init__(
        self,
        libdoc: LibraryDoc,
        datatypes: DatatypeStorage,
        pk_generator: PKGenerator,
        uid_generator: UidGenerator,
    ) -> None:
        self.libdoc = libdoc
        self.datatypes = datatypes
        self.pk_generator = pk_generator
        self.uid_generator = uid_generator
        self.parameter_name_prefix = {
            ArgInfo.VAR_POSITIONAL: "* ",
            ArgInfo.VAR_NAMED: "** ",
            ArgInfo.NAMED_ONLY: "- ",
        }
        self._ordering = -1024
        self.argument_kind_default = {
            ArgInfo.VAR_POSITIONAL: "@{EMPTY}",
            ArgInfo.VAR_NAMED: "&{EMPTY}",
        }

    @property
    def ordering(self):
        self._ordering += 1024
        return self._ordering

    def get_interaction_from_keyword(
        self, keyword: KeywordDoc, reference_pk: Optional[str]
    ) -> Interaction:
        references = (
            References(reference_ref=[Ref(pk=reference_pk)]) if reference_pk else References()
        )
        return create_interaction(
            pk=self.pk_generator.get_pk(),
            name=keyword.name,
            uid=self.uid_generator.get_uid(
                TestElementType.INTERACTION, keyword.name, self.libdoc.name
            ),
            # html_description=f"<html>{keyword.doc.replace('<br>', '<br/>').replace('<hr>', '<br/>')}</html>",
            references=references,
            parameters=self.get_interaction_parameters(keyword),
        )

    def get_return_type_parameter(self, keyword: KeywordDoc) -> Optional[Parameter]:
        keyword_dict = keyword.to_dictionary()
        if not keyword_dict.get('returnType'):
            return None
        return Parameter(
            pk=self.pk_generator.get_pk(),
            name="return_value",
            definition_type=DefinitionType.DETAILED,
            use_type=UseType.CALL_BY_REFERENCE,
            default_value=DefaultValue(
                type_value="1",
                type_attribute=DefaultValueType.REPRESENTATIVE,
                representative_ref=Ref(
                    pk=self.datatypes.get_equivalence_class(
                        "assigned_variable", "no_assignment", False
                    )
                    .representatives.representative[0]
                    .pk
                ),
            ),
            datatype_ref=Ref(pk=self.datatypes.get_datatype("assigned_variable").pk),
        )

    def get_argument_types(self, argument_type: TypeInfo) -> List[TypeInfo]:
        try:
            types = []
            if argument_type.is_union:
                for type in argument_type.nested:
                    types.extend(self.get_argument_types(type))
                return types
        except AttributeError:  # above block does not work for rf5
            return [argument_type]
        return [argument_type]

    def get_interaction_parameters(self, keyword: KeywordDoc) -> Parameters:
        parameters = Parameters(parameter=[])
        return_parameter = self.get_return_type_parameter(keyword)
        if return_parameter:
            parameters.parameter.append(return_parameter)
        for argument in keyword.args:
            if (
                not argument.kind
                or argument.kind == ArgInfo.POSITIONAL_ONLY_MARKER
                or argument.kind == ArgInfo.NAMED_ONLY_MARKER
                or argument.kind == NOT_SET
            ):
                continue
            try:
                arg_type_names = [
                    arg_type.name for arg_type in self.get_argument_types(argument.type)
                ]
            except AttributeError:
                arg_type_names = [arg_type.name for arg_type in self.get_argument_types(argument)]
            for arg_type in arg_type_names:
                datatype = self.datatypes.get_datatype(arg_type)
                break
            if not datatype:
                datatype = self.datatypes.get_datatype(argument.name)
            if not datatype:
                if argument.default_repr or self.argument_kind_default.get(argument.kind):
                    datatype = self.datatypes.get_datatype("default_value")
            datatype_pk = datatype.pk if datatype else "-1"

            parameter = Parameter(
                pk=self.pk_generator.get_pk(),
                name=f"{self.parameter_name_prefix.get(argument.kind, '')}{argument.name}",
                datatype_ref=Ref(pk=datatype_pk),
                definition_type=DefinitionType.DETAILED,
                use_type=UseType.CALL_BY_VALUE,
            )
            default_value = argument.default_repr or self.argument_kind_default.get(argument.kind)

            repr = (
                self.datatypes.get_representative(datatype.name, default_value)
                if datatype
                else None
            )
            if repr:
                parameter.default_value = DefaultValue(
                    type_value="1",
                    representative_ref=Ref(pk=repr.pk),
                    type_attribute=DefaultValueType.REPRESENTATIVE,
                )
            parameters.parameter.append(parameter)
        return parameters
