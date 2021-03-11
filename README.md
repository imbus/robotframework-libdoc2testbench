# robotframework-libdoc2testbench
Robot Framework Libdoc Extension that generates imbus TestBench Library import formats.
___

**Installation**:

	pip install robotframework-libdoc2testbench
___
**Usage**:

The basic usage just needs the ``Libdoc2TestBench`` command and a Robot Framework Library as input and saves a zip-file named "project-dump.zip" in the current working directory containing the needed information for the import.

	Libdoc2TestBench <LIBRARY or *.robot or *.py>
By using a second positional argument you can additionally specify the output filename:

	Libdoc2TestBench <LIBRARY or *.robot or *.py> <output.zip>


The generated zip-file can be imported via the "Import Project..." command in the Project Management view of the imbus TestBench.

___

There are several optional arguments, that follow the structure of the robot.libdoc module. When generating imports from a RF library, these values should already be set up correctly. You may overwrite the docformat by setting the associated arguments written below.

| Arguments 	| Description 	| Allowed Values 	|
|-	|-	|-	|
| -s, --specdocformat 	| Specifies the documentation format used with XML and JSON spec files.  `RAW` means preserving the original documentation format and `HTML` means converting documentation to HTML.  The default is `HTML`. 	| `HTML`, `RAW` 	|
| -F, --docformat 	| Specifies the source documentation format.  Possible values are Robot Framework's documentation format, HTML, plain text, and reStructuredText.  The default value can be specified in library source code and the initial default value is `ROBOT`. 	| `ROBOT`, `HTML`, `TEXT`, `REST` 	|
| -n, --name 	| Sets the name of the documented library or resource for the import. 	|  	|
| -v, --version 	| Sets the version of the documented library or resource written for the import written in the description. 	|  	|
___
**Dependencies**:
 - python >=3.7
 - [robotframework](https://github.com/robotframework/robotframework) > 3.2.2