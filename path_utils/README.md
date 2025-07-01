# path_utils - Path Utilities

[日本語 Readme](./README.ja.md)

## 1. Overview

Utility functions for file paths.

## 2. Key Features

- Obtain an absolute path from a project-root-relative path
  - Absorbing differences such as running a Python script vs an EXE file, and variations in the current working directory
- Retrieve the absolute path of the project root directory
- Retrieve the absolute path of the internal root directory when running as an EXE file

## 3. Installation

Place the following file under `util/` (or your preferred package directory):

- [path_utils - Path Utilities](./path_utils.py)

## 4. Usage

Call as in the example below.

```python
import util.path_utils as path_utils

env_file_path = path_utils.runtime_path(".env")
setting_file_path = path_utils.runtime_path("data/setting.txt")
```

## 5. Dependencies & Verified Versions

- Python 3.12.10

## 6. Repository

- [Bubbles877/python-utilities](https://github.com/Bubbles877/python-utilities)
