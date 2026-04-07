---
sidebar_position: 3
---

# Command Line Arguments

This page documents the command-line interface for Libdoc2TestBench.

:::tip
For detailed explanations of all configuration options, see [Configuration Options](options.md).
:::

## Basic Syntax

```bash
Libdoc2TestBench <LIBRARY|PATH> [OUTPUT] [OPTIONS]
```

## Positional Arguments

| Argument | Description |
|----------|-------------|
| `LIBRARY\|PATH` | Robot Framework library name, path to a Python file, resource file, or directory |
| `OUTPUT` | Optional output filename (default: `<library_name>.zip`) |

## Help and Version

| Argument | Description |
|----------|-------------|
| `-h`, `--help` | Show help message and exit |
| `--version`, `--info` | Display Libdoc2TestBench, Robot Framework, and Python versions |

## Quick Reference

### Documentation Options

### Documentation Options

| Argument | Values | Default |
|----------|--------|---------|
| `-F <FORMAT>`, `--documentation-format <FORMAT>` | `ROBOT`, `HTML`, `TEXT`, `REST` | `ROBOT` |
| `-s <FORMAT>`, `--specification-format <FORMAT>` | `HTML`, `RAW` | `HTML` |

### Structure Options

| Argument | Default |
|----------|---------|
| `--library-root <NAME>` | `RF` |
| `--resource-root <NAME>` | `Resource` |
| `-r <ID>`, `--repository <ID>` | `iTB_RF` |

### Naming Options

| Argument | Default |
|----------|---------|
| `--library-name-extension <EXT>` | `[Robot-Library]` |
| `--resource-name-extension <EXT>` | `[Robot-Resource]` |

### Datatype Options

| Argument | Values | Default |
|----------|--------|---------|
| `--created-datatypes <MODE>` | `ALL`, `ENUMS`, `NONE` | `ENUMS` |

### File Options

| Argument | Default |
|----------|---------|
| `-a`, `--attachment` | `false` |
| `--excluded-paths <PATTERNS>` | `[]` |

## Examples

### Basic Library Import

```bash
Libdoc2TestBench BuiltIn
```

### Custom Output Name

```bash
Libdoc2TestBench Collections MyCollections.zip
```

### Import Custom Library with Options

```bash
Libdoc2TestBench mycustomlib.py --library-root "CustomLibs" --created-datatypes ALL
```

### Import Directory with Exclusions

```bash
Libdoc2TestBench ./libraries/ --excluded-paths "**/__pycache__/**" "**/test_*.py"
```
Usage 
### Import Resource with Attachment

```bash
Libdoc2TestBench keywords.resource --attachment
```

### Override Documentation Format

```bash
Libdoc2TestBench MyLibrary --documentation-format HTML
```

### Full Example with Multiple Options

```bash
Libdoc2TestBench ./my_libs/ MyProject.zip \
  --library-root "RobotLibs" \
  --library-name-extension "[RF]" \
  --created-datatypes ALL \
  --repository "MyProject_RF" \
  --excluded-paths "**/test_*.py"
```

## Using with Configuration Files

All command-line arguments can also be specified in a `pyproject.toml` file. See [Configuration File](config_file.md) for details.

Command-line arguments override configuration file settings, allowing you to customize individual runs while maintaining project defaults.
