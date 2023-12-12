from typing import List, Optional

from robot.running.arguments.argumentspec import ArgInfo

try:
    from robot.utils import NOT_SET
except ImportError:
    NOT_SET = ArgInfo.NOTSET


def _get_arg_sub_types(arg_type):
    type_names = []
    if arg_type.is_union:
        for arg_type in arg_type.nested:
            type_names.extend(_get_arg_sub_types(type))
        return type_names
    return [arg_type.name]


def get_argument_type_names(argument: ArgInfo) -> List[str]:
    try:
        argument_type = argument.type
    except:
        argument_type = argument  # above block does not work for rf5
    try:
        type_names = []
        if argument_type.is_union:
            for type in argument_type.nested:
                type_names.extend(_get_arg_sub_types(type))
            return type_names
    except AttributeError:  # above block does not work for rf5
        return [argument_type.name]
    return [argument_type.name]


def get_arg_kind_default_value(argument_kind: str) -> Optional[str]:
    if argument_kind == ArgInfo.VAR_POSITIONAL:
        return "@{EMPTY}"
    if argument_kind == ArgInfo.VAR_NAMED:
        return "&{EMPTY}"
    return None


def requires_datatype_creation(argument) -> bool:
    argument_kind = argument.kind
    if (
        not argument_kind
        or argument_kind == ArgInfo.POSITIONAL_ONLY_MARKER
        or argument_kind == ArgInfo.NAMED_ONLY_MARKER
        or argument_kind == NOT_SET
    ):
        return False
    return True
