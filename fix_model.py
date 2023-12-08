import re
import sys
from pathlib import Path

py_model = Path(sys.argv[1])
if not py_model.exists():
    raise Exception(f"File {py_model} does not exist")

with open(py_model) as f:
    model = f.readlines()
    fixed_model = []
    enum_started = False
    enum_members = {}
    for line in model:
        if "(Enum):" in line:
            print(line)
            enum_started = True
            fixed_model.append(line)
            continue
        doc_match = re.fullmatch(r".*:cvar (?P<member>VALUE_\d*): (?P<name>.*)\n", line)
        if enum_started and doc_match:
            enum_members[doc_match.group("member")] = doc_match.group("name")
            fixed_model.append(line)
            continue
        member_match = re.fullmatch(
            r"(?P<indent>\s*)(?P<member>VALUE_\d*) = (?P<value>\d*)\n", line
        )
        if enum_started and member_match:
            new_line = f"{member_match.group('indent')}{enum_members.pop(member_match.group('member'))} = {member_match.group('value')}\n"
            print(new_line)
            fixed_model.append(new_line)
            if not enum_members:
                enum_started = False
            continue
        fixed_model.append(line)

with open(py_model, "w") as f:
    f.writelines(fixed_model)
