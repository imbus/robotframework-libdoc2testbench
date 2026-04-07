---
sidebar_position: 2
---

# Configuration File

Libdoc2TestBench supports configuration via `pyproject.toml`, allowing you to define default settings for your project instead of passing command-line arguments every time.

:::tip
For a complete list of all available options, see [Configuration Options](options.md).
:::

## Using pyproject.toml

Add a `[tool.libdoc2testbench]` section to your `pyproject.toml` file with your desired configuration options.

### Basic Example

```toml
[tool.libdoc2testbench]
created_datatypes = "ENUMS"
library_root = "Robot"
resource_root = "Robot"
```

### Complete Example

```toml
[tool.libdoc2testbench]
# Datatype creation
created_datatypes = "ENUMS"

# Structure organization
library_root = "RobotLibraries"
resource_root = "RobotResources"
library_name_extension = "[RF-Lib]"
resource_name_extension = "[RF-Res]"

# Repository identification
repository = "MyProject_RF"

# File handling
attachment = true
excluded_paths = [
  "**/test_*.py",
  "**/experimental/**",
  "**/__pycache__/**"
]

# Documentation formats
documentation_format = "ROBOT"
specification_format = "HTML"
```

## Option Names

In `pyproject.toml`, use the full option names without the `--` prefix. For example:
- CLI: `--created-datatypes ALL`
- TOML: `created_datatypes = "ALL"`

Boolean flags use `true`/`false`:
- CLI: `--attachment`
- TOML: `attachment = true`

## Overriding Configuration

Command-line arguments always take precedence over configuration file settings.

**Example:**

```bash
# Uses settings from pyproject.toml
Libdoc2TestBench MyLibrary

# Overrides created_datatypes to ALL
Libdoc2TestBench MyLibrary --created-datatypes ALL
```

## Configuration File Location

Libdoc2TestBench looks for `pyproject.toml` in:
1. The current working directory
2. Parent directories (traversing up the directory tree)

This allows you to place the configuration at your project root.
