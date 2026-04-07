---
sidebar_position: 1
---

# Advanced Usage

This page covers advanced usage patterns and features of Libdoc2TestBench.

## Excluding Keywords from Import

Sometimes you don't want to import every single keyword of a custom library or resource file into TestBench. To mark keywords that should not be imported, add a tag to those keywords.

You can use either:
- The Robot Framework built-in tag **`robot:private`**
- The custom tag **`tb:ignore`**

**Example:**

```robotframework
*** Keywords ***
Public Keyword
    [Documentation]    This keyword will be imported
    Log    This is a public keyword

Private Keyword
    [Documentation]    This keyword will NOT be imported
    [Tags]    robot:private
    Log    This is a private keyword

Internal Helper
    [Documentation]    This keyword will also NOT be imported
    [Tags]    tb:ignore
    Log    This is an internal helper
```

## Linking Keywords to Existing TestBench keywords

If an interaction already exists in TestBench and you want to link a Robot Framework keyword to it (rather than creating a new interaction), use the **`tb:uid:<unique_id>`** tag.

This sets the specific unique ID with which the keyword should be imported, preventing duplication.

**Example:**

```robotframework
*** Keywords ***
Login To System
    [Documentation]    Logs in to the system
    [Tags]    tb:uid:12345678-1234-1234-1234-123456789abc
    [Arguments]    ${username}    ${password}
    # Keyword implementation here
```

## Importing Directory Structures

When you specify a directory path, Libdoc2TestBench recursively searches all subdirectories and preserves the directory structure in TestBench.

**Example directory structure:**

```
my_libraries/
├── web/
│   ├── login.py
│   └── navigation.py
└── api/
    ├── rest_client.py
    └── soap_client.py
```

**Command:**

```bash
Libdoc2TestBench my_libraries/
```

This creates a TestBench structure that mirrors your directory layout, making it easier to organize and locate your keywords.

## Importing Resource Files

Resource files (`.robot` or `.resource`) can be imported just like Python libraries:

```bash
Libdoc2TestBench myresource.resource
```

Use the `-a` or `--attachment` flag to attach the resource file to the generated keywords:

```bash
Libdoc2TestBench myresource.resource -a
```

## Custom Output Names

Specify a custom name for the generated zip file:

```bash
Libdoc2TestBench Collections MyCustomCollections.zip
```

## Specifying Documentation Format

Override the source documentation format with the `-F` or `--documentation-format` option:

```bash
Libdoc2TestBench MyLibrary -F HTML
```

Supported formats:
- `ROBOT` (default)
- `HTML`
- `TEXT`
- `REST` (reStructuredText)
