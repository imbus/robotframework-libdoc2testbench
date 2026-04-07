---
sidebar_position: 1
---

# Libdoc2TestBench

**Libdoc2TestBench** is a Robot Framework Libdoc extension that generates import formats compatible with imbus [TestBench](https://www.imbus.de/en/testbench-enterprise). It enables you to import Robot Framework libraries and resource files into TestBench as keywords and datatypes.

## Overview

This tool converts Robot Framework libraries and resource files into TestBench-compatible format, allowing you to:

1. **Import official Robot Framework libraries** (e.g., BuiltIn, Collections, String)
2. **Import custom Robot Framework libraries** from your Python modules
3. **Import Robot Framework resource files**

## Key Features

- ✅ Generate TestBench keywords from Robot Framework keywords
- ✅ Create TestBench datatypes from Robot Framework type hints
- ✅ Flexible configuration via CLI or `pyproject.toml`
- ✅ Directory structure preservation for organized imports

## Requirements

- **Python 3.9 or higher**
- **Robot Framework 5.0.0 or higher**

:::info
This extension requires Robot Framework 5.0.0 or later and does not work with earlier versions.
:::


