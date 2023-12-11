from typing import List


try:
    from robot.running.arguments.typeinfo import TypeInfo
except ImportError:
    try:
        from robot.running.arguments.argumentspec import TypeInfo
    except ImportError:
        from robot.running.arguments.argumentspec import ArgInfo as TypeInfo


def get_argument_type_names(argument_type: TypeInfo) -> List[TypeInfo]:
    try:
        type_names = []
        if argument_type.is_union:
            for type in argument_type.nested:
                type_names.extend(get_argument_type_names(type))
            return type_names
    except AttributeError:  # above block does not work for rf5
        return [argument_type.name]
    return [argument_type.name]
