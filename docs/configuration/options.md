---
sidebar_position: 1
---

# Configuration Options

This page documents all available configuration options for Libdoc2TestBench. These options can be used both in command-line arguments and in `pyproject.toml` configuration files.

## Common Options

| Option | CLI Argument | Description | Default |
|--------|--------------|-------------|---------|
| `created_datatypes` | `--created-datatypes <MODE>` | Datatype creation mode | `ENUMS` |
| `library_root` | `--library-root <NAME>` | Subdivision name for imported libraries | `RF` |
| `resource_root` | `--resource-root <NAME>` | Subdivision name for imported resources | `Resource` |
| `library_name_extension` | `--library-name-extension <EXT>` | Extension added to library subdivision names | `[Robot-Library]` |
| `resource_name_extension` | `--resource-name-extension <EXT>` | Extension added to resource subdivision names | `[Robot-Resource]` |
| `repository` | `-r, --repository <ID>` | Repository ID in TestBench import | `iTB_RF` |
| `excluded_paths` | `--excluded-paths <PATTERNS>` | Paths or glob patterns to ignore | `[]` |
| `attachment` | `-a, --attachment` | Attach resource files to interactions | `false` |

## Documentation Options

| Option | CLI Argument | Description | Default |
|--------|--------------|-------------|---------|
| `documentation_format` | `-F, --documentation-format <FORMAT>` | Source documentation format | `ROBOT` |
| `specification_format` | `-s, --specification-format <FORMAT>` | Format for XML/JSON specs | `HTML` |

### Documentation Formats

- **`ROBOT`** - Robot Framework's native documentation format (default)
- **`HTML`** - HTML formatted documentation
- **`TEXT`** - Plain text documentation
- **`REST`** - reStructuredText formatted documentation

### Specification Formats

- **`HTML`** - Convert documentation to HTML (default)
- **`RAW`** - Preserve original documentation format

## Datatype Creation Modes

The `created_datatypes` option controls how Robot Framework type hints are converted to TestBench datatypes:

- **`ALL`** - Create datatypes for all Robot Framework types
- **`ENUMS`** - Create only enum types (default, recommended)
- **`NONE`** - Skip datatype creation, use generic parameters only

### When to Use Each Mode

**Use `ENUMS` (recommended):**
- For most projects
- When you want type safety for enumerated values
- Balances type information with simplicity

**Use `ALL`:**
- When you need full type information in TestBench
- For complex libraries with many custom types
- When strict type checking is required

**Use `NONE`:**
- For simple libraries without type hints
- When you prefer generic parameters
- To simplify the TestBench import

## Path Options

### Library and Resource Roots

The `library_root` and `resource_root` options define the subdivision names in TestBench where imported libraries and resources are organized.

**Example:**
```toml
library_root = "RobotLibraries"
resource_root = "RobotResources"
```

This creates a clear separation between libraries and resources in the TestBench hierarchy.

### Name Extensions

The `library_name_extension` and `resource_name_extension` options add suffixes to subdivision names in TestBench.

**Common Use Case:** Integration with testbench2robotframework

If you set:
```toml
library_name_extension = "[RF-Lib]"
resource_name_extension = "[RF-Res]"
```

Then in `testbench2robotframework`, you can use regex patterns to filter:
```toml
rfLibraryRegex = ".*\\[RF-Lib\\]"
rfResourceRegex = ".*\\[RF-Res\\]"
```

This ensures only Robot Framework elements are processed during test execution.

### Excluding Paths

Use the `excluded_paths` option to exclude specific files or directories from import. Supports glob patterns:

**Examples:**
```toml
excluded_paths = [
  "**/test_*.py",           # Exclude test files
  "**/experimental/**",     # Exclude experimental directory
  "**/__pycache__/**",      # Exclude Python cache
  "**/.git/**"              # Exclude git directory
]
```

Patterns are relative to the current working directory.

## Repository ID

The `repository` option sets the repository identifier in the TestBench import XML. This is useful when managing multiple Robot Framework projects in TestBench.

**Example:**
```toml
repository = "MyProject_RF"
```

## Attachment Option

The `attachment` option controls whether resource files are attached to the generated TestBench interactions.

**When to use:**
- Set to `true` when importing resource files that you want to keep linked
- Helps maintain traceability between TestBench and Robot Framework
- Useful for documentation purposes

**Note:** Only applies to resource file imports, not Python library imports.

## Using Options

Configuration options can be specified in two ways:

1. **Command-line arguments** - See [Command Line Arguments](commands.md)
2. **Configuration file** - See [Configuration File](config_file.md)

Command-line arguments take precedence over configuration file settings.
