import re
import sys
from typing import ClassVar, List, Optional

from robot.libdocpkg.model import KeywordDoc
from robot.libdocpkg.robotbuilder import LibraryDoc


class SpecialTags:
    found_uids: ClassVar = []

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
                uid = match.group('uid')
                if uid in self.found_uids:
                    sys.exit(
                        f"""ERROR: Tag 'tb:uid:{uid}' is used in multiple keywords.
                              Project import stopped..."""
                    )
                self.found_uids.append(uid)
                return uid
        return None
