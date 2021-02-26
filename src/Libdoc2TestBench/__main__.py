import sys
from os import path
from Libdoc2TestBench import create_project_dump

if __name__ == "__main__":
    print(sys.argv[0])
    if len(sys.argv) == 3:
        create_project_dump(sys.argv[1], sys.argv[2])
    else:
        pass
        # RBGLibrary out.xml
