import re
from typing import List, Optional

from robot.libdocpkg.model import KeywordDoc
from robot.libdocpkg.robotbuilder import LibraryDoc


class SpecialTags:
    def __init__(self, libdoc: LibraryDoc) -> None:
        self.libdoc = libdoc

    def get_ignored_keywords(self) -> List[str]:
        return [
            keyword.name
            for keyword in self.libdoc.keywords
            if "robot:private" in keyword.tags or "tb:ignore" in keyword.tags
        ]

    def get_uid(self, keyword: KeywordDoc) -> Optional[str]:
        for tag in keyword.tags:
            match = re.match(r"^tb:uid:(?P<uid>.*)", tag)
            if match:
                return match.group('uid')
        return None
