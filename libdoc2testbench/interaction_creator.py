from typing import Optional

from robot.libdocpkg.model import KeywordDoc
from robot.libdocpkg.robotbuilder import LibraryDoc
from robot.running.arguments.argumentspec import ArgInfo

from libdoc2testbench.datatype_creator import DatatypeCreator
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
        self, libdoc: LibraryDoc, pk_generator: PKGenerator, uid_generator: UidGenerator
    ) -> None:
        self.libdoc = libdoc
        self.pk_generator = pk_generator
        self.uid_generator = uid_generator
        self.parameter_name_prefix = {
            ArgInfo.VAR_POSITIONAL: "* ",
            ArgInfo.VAR_NAMED: "** ",
            ArgInfo.NAMED_ONLY: "- ",
        }
        self._ordering = -1024

    @property
    def ordering(self):
        self._ordering += 1024
        return self._ordering

    def get_interaction_from_keyword(
        self, keyword: KeywordDoc, datatype_creator: DatatypeCreator, reference_pk: Optional[str]
    ) -> Interaction:
        self.datatype_creator = datatype_creator
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
                representative_ref=Ref(pk=self.datatype_creator.return_value_default_repr),
            ),
            datatype_ref=Ref(pk=self.datatype_creator.return_value_datatype_pk),
        )

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
            datatype_pk = "-1"
            if not self.datatype_creator.argument_corresponds_to_enum(
                argument
            ) and not self.datatype_creator.argument_corresponds_to_typed_dict(argument):
                datatype = next(
                    filter(
                        lambda datatype: datatype.name == argument.name,
                        self.datatype_creator.standard_types,
                    ),
                    None,
                )
                if not datatype and argument.default_repr:
                    datatype = self.datatype_creator.default_datatype
                datatype_pk = datatype.pk if datatype else "-1"
            else:
                for arg_type in self.datatype_creator.get_argument_types(argument.type):
                    datatype = next(
                        filter(
                            lambda dt: dt.name == arg_type.name,
                            [*self.datatype_creator.enums, *self.datatype_creator.typed_dicts],
                        ),
                        None,
                    )
                    if not datatype and argument.default_repr:
                        datatype = self.datatype_creator.default_datatype
                    if datatype:
                        datatype_pk = datatype.pk
                        break
            parameter = Parameter(
                pk=self.pk_generator.get_pk(),
                name=f"{self.parameter_name_prefix.get(argument.kind, '')}{argument.name}",
                datatype_ref=Ref(pk=datatype_pk),
                definition_type=DefinitionType.DETAILED,
                use_type=UseType.CALL_BY_VALUE,
            )
            default_value = (
                argument.default_repr
                or self.datatype_creator.get_arg_kind_default_value(argument.kind)
            )
            repr = (
                next(
                    filter(
                        lambda representative: representative.name == default_value,
                        [
                            repr
                            for eq in datatype.equivalence_classes.equivalence_class
                            for repr in eq.representatives.representative
                        ],
                    ),
                    None,
                )
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
