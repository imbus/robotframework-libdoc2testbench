from enum import Enum

from robot.running.arguments.argumentspec import ArgInfo
from robot.utils import safe_str

try:
    from robot.utils import NOT_SET
except ImportError:
    NOT_SET = ArgInfo.NOTSET

__version__ = "1.2.1"


def default_repr(self):
    if self.default is NOT_SET:
        return None
    if isinstance(self.default, (bool, int, float)) or self.default is None:
        return f"${{{self.default}}}"
    if self.default == "":
        return "${Empty}"
    if isinstance(self.default, Enum):
        return self.default.name
    return safe_str(self.default)


ArgInfo.default_repr = property(default_repr)
