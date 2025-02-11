# Libdoc2TestBench
Robot Framework Libdoc extension that generates [TestBench](https://www.testbench.com) import formats.
It can be used to generate Testbench interactions and datatypes from Robotframework libraries.
___

### Installation:

To install this package you can use the following `pip` command:

```bash
pip install robotframework-libdoc2testbench
```

*Notice: This extension requires Robot Framework 5.0.0 or later and does not work with earlier versions.*
___
### Usage:

There are three main use cases:
* Import official Robot Framework librarys
* Import custom Robot Framework librarys
* Import Robot Framework resource files

#### Import official Robot Framework librarys

![LibDoc2TestBench command demo](res/example_usage.gif)

For the most basic usage you just have to pass a Robot Framework library as an argument to the ``Libdoc2TestBench`` command.
``Libdoc2TestBench`` will create a zip-file with the name of the library in the current working directory. This zip-file can be imported to TestBench in order to use Robot Framework keywords from within TestBench.

```bash
Libdoc2TestBench <LIBRARY>
```
The `<LIBRARY>` argument corresponds to the Robot Framework library name that you would use to import the library in the ``*** Settings ***`` of a robot/resource file.
The second positional argument can be used to specify the name of the generated zip-file:

```bash
Libdoc2TestBench <LIBRARY> <output.zip>
```

#### Import the generated TestBench zip-file
The generated zip-file can be imported via the `Import Project...` command in the Project Management view of the imbus TestBench:

![Import Project Demo](res/projectmanagement_view.gif)

Afterwards you'll find your imported RF library, the different interactions and the datatypes in the Test Elements view:

![Test Element View](res/test_element_view.png)

The imported Testelements can be copied into another testbench project. When copying, it is important that the test elements remain in the same subdivisions.

#### Import custom robotframework librarys

Libdoc2Testbench can also be used to import custom Robot Framework librarys.

Example for a custom library:
```python
class mycustomlibrary(object):
    def print_hello_world(self):
        print("Hello World")
```

Example Libdoc2Testbench usage:

```bash
Libdoc2TestBench mycustomlibrary.py
```

#### Import Robot Framework resource files

Libdoc2Testbench can also be used to import Robot Framework resource files.

Example for a resource file:

```robotframework
*** Keywords ***
print hello world
	log	Hello World
```

Example Libdoc2Testbench usage:

```bash
Libdoc2TestBench path/to/keywords.resource
```

#### Importing multiple librarys and resource files at once

Libdoc2Testbench can be used to import multiple librarys and resource files at once. A special robot framework section is used for this use case.

Example for a import List:

```robotframework
*** Import List ***
BrowserLibrary
BuiltIn
mycustomlibrary.py
myresource.resource
```

Example Libdoc2Testbench usage:

```bash
Libdoc2TestBench importlist.robot
```

___
### Command line arguments
There are several optional arguments, that follow the structure of the robot.libdoc module. When generating imports from a RF library, these values should already be set up correctly. You may overwrite the docformat and other meta data by setting the associated arguments written below.

| Arguments 	| Description 	| Allowed Values 	|
|-	|-	|-	|
| `-h`, `--help` | Show the help message and exit
| `-a`, `--attachment` |  Defines if the resource file, which has been used to generate the interactions, will be attached to those interactions.
| `-F FORMAT`, `--docformat FORMAT` 	| Specifies the source documentation format.  Possible values are Robot Framework's documentation format, HTML, plain text, and reStructuredText.  The default value can be specified in library source code and the initial default value is `ROBOT`. 	| `ROBOT` `HTML` `TEXT` `REST` 	|
| `--libraryroot LIBRARYROOT`| Defines the subdivision name which contains the imported Robot Framework libraries. Default is ``RF``.
| `--resourceroot RESOURCEROOT` |Defines the subdivision name which contains the imported Robot Framework resources. Default is ``Resource``.
| `--libversion LIBVERSION` | Sets the version of the documented library or resource written in the description.
| `--libname` 	| Sets the name of the documented library or resource. 	|  	|
| `-r REPOSITORY`, `--repository REPOSITORY`| Sets the repository id of the TestBench import. The default is `iTB_RF`.||
| `-s SPECFORMAT`, `--specdocformat SPECFORMAT` 	| Specifies the documentation format used with XML and JSON spec files.  `RAW` means preserving the original documentation format and `HTML` means converting documentation to HTML.  The default is `HTML`. 	| `HTML` `RAW` 	|
| `--version`, `--info` 	| Writes the Libdoc2TestBench, Robot Framework and Python version to console. 	|  	|
| `--library_name_extension` | Adds an extension to the name of an Robot Framework library subdivision in TestBench. Often used in combination with the `rfLibraryRegex` in `testbench2robotframework`.  Default is `[Robot-Library]`.||
| `--resource_name_extension` | Adds an extension to the name of an Robot Framework resource subdivision in TestBench. Often used in combination with the `rfResourceRegex` in `testbench2robotframework`. Default is `[Robot-Resource]`.||
| `--created_datatypes` | Option to specify if all Robot Framework datatypes should be created in TestBench (`ALL`), only the enum types (`ENUM`) or if no datatype should be created and only generic parameters are used (`NONE`). The default is `ALL`. ||
___

### Change log
* 1.2
    * Added library keyword return types with RobotFramework version >= 7
    * Added datatype creation options with default values
    * Removed `--xml` cli option
    * Removed `--temp` cli option
* 1.1
    * Added TestBench datatypes
    * Added default values
* 1.0rc2
    * ADDED optional arguments for:
        * xml-file output (instead of zip-file)
        * custom temporary directory
        * changing the repository id in the xml-header
        * custom primary key enumeration start
        * info command for printing Libdoc2TestBench/Robot Framework/Python version to console
        * support for resource-files (attachment support coming soon)
    * FIX:
        * only create `_Datatype` subdivison in libraries when data types are present
        * `Resource` subdivison is now in the correct parent subdivision
        * Updated README.md / package help-messages to reflect changes
* 1.0rc1
    * first release candidate

___
### License
Distributed under the [Apache-2.0 license](https://github.com/imbus/robotframework-libdoc2testbench/blob/main/LICENSE). See [LICENSE](LICENSE) for more information.
___
### Dependencies
 - python >= 3.8
 - [robotframework](https://github.com/robotframework/robotframework) >= 5.0.0
