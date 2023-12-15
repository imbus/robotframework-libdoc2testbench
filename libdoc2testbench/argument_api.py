from itertools import chain
from typing import List, Optional

from robot.running.arguments.argumentspec import ArgInfo

try:
    from robot.utils import NOT_SET
except ImportError:
    NOT_SET = ArgInfo.NOTSET


def _get_arg_sub_types(arg_type) -> List:
    if not arg_type.is_union:
        return [arg_type.name]
    nested_types = [_get_arg_sub_types(nested_type) for nested_type in arg_type.nested]
    return list(chain.from_iterable(nested_types))


def get_argument_type_names(argument: ArgInfo) -> List[str]:
    try:
        return _get_arg_sub_types(argument.type)
    except AttributeError:
        return [argument.name]  # above block does not work for rf5


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
