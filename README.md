# Libdoc2TestBench
Robot Framework Libdoc Extension that generates imbus [TestBench Enterprise](https://www.imbus.de/testbench/testbench-enterprise) Library import formats.

___

### Installation:

To install this package you can use  `pip`:

	pip install robotframework-libdoc2testbench

*Notice: This extension requires Robot Framework 4.0.0 or later and does not work with earlier versions.*
___
### Usage:
![LibDoc2TestBench command demo](res/example_usage.gif)

The basic usage just needs the ``Libdoc2TestBench`` command and a Robot Framework Library as input and saves a zip-file named `project-dump.zip` in the current working directory containing the needed information for the import.

```bash
Libdoc2TestBench <LIBRARY or RESOURCE>
```
By using a second positional argument you can additionally specify the output filename:

	Libdoc2TestBench <LIBRARY or RESOURCE> <output.zip>
___

There are several optional arguments, that follow the structure of the robot.libdoc module. When generating imports from a RF library, these values should already be set up correctly. You may overwrite the docformat and other meta data by setting the associated arguments written below.

| Arguments 	| Description 	| Allowed Values 	|
|-	|-	|-	|
| `-s`, `--specdocformat` 	| Specifies the documentation format used with XML and JSON spec files.  `RAW` means preserving the original documentation format and `HTML` means converting documentation to HTML.  The default is `HTML`. 	| `HTML` `RAW` 	|
| `-F`, `--docformat` 	| Specifies the source documentation format.  Possible values are Robot Framework's documentation format, HTML, plain text, and reStructuredText.  The default value can be specified in library source code and the initial default value is `ROBOT`. 	| `ROBOT` `HTML` `TEXT` `REST` 	|
| `-n`, `--name` 	| Sets the name of the documented library or resource for the import. 	|  	|
| `-v`, `--version` 	| Sets the version of the documented library or resource written for the import written in the description. 	|  	|
| `-r`, `--repository`| Sets the repository id of the TestBench import. The default is `itba`||
| `--info` | Writes the Libdoc2TestBench, Robot Framework and Python version to console.||
___

### Import in imbus TestBench
First create a zip-file from a Robot Framework library via the `Libdoc2TestBench` command.
Afterwards the generated zip-file can be imported via the `Import Project...` command in the Project Management view of the imbus TestBench:

![Import Project Demo](res/projectmanagement_view.gif)

In the Test Elements view you can now see your imported RF library as different interactions and datatypes:

![Test Element View](res/test_element_view.png)

<!-- ### Change log
* 0.0.1
    * working first version -->

___
### License
Distributed under the [Apache-2.0 license](https://github.com/imbus/robotframework-libdoc2testbench/blob/main/LICENSE). See [LICENSE](LICENSE) for more information.
___
### Dependencies:
 - python >=3.7
 - [robotframework](https://github.com/robotframework/robotframework) >= 4.0.0