# robotframework-libdoc2testbench
Robot Framework Libdoc Extension that generates imbus TestBench Library import formats.
___

**Installation**:

	pip install robotframework-libdoc2testbench
___
**Usage**:

The basic usage just needs a Robot Framework Library and saves a zip-file named "project-dump.zip" in the current working directory containing the needed information for the import.

	python -m Libdoc2TestBench <LIBRARY or *.robot or *.py>
By using the optional paramter --outfile_path (-o) you can additionally specify the output filename:

	python -m Libdoc2TestBench <LIBRARY or *.robot or *.py> -o <output.zip>


The generated zip-file can be imported via the "Import Project..." command in the Project Management view of the imbus TestBench.
___
**Dependencies**:
 - python >=3.7
 - [robotframework](https://github.com/robotframework/robotframework) > 3.2.2