# Python - Input/Output

This project focuses on Python file handling and JSON serialization/deserialization. It covers reading and writing text files safely using context managers (`with`), and working with JSON as a data interchange format.

## Learning Objectives

- Open, read, and write files in Python
- Ensure files are properly closed using the `with` statement
- Read full file content and read line by line
- Understand JSON, serialization, and deserialization
- Convert between Python objects and JSON strings
- Access command-line arguments in Python scripts

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- First line of each file: `#!/usr/bin/python3`
- Code style: `pycodestyle` (2.7.*)
- All files must be executable and end with a new line
- Documentation is required for modules, classes, and functions
- Test files (when required) must be in `tests/` and run with:
  - `python3 -m doctest ./tests/*`

**Constraints:**
- Must use the `with` statement
- No module imports allowed
- No need to handle missing file/permission exceptions

**Prototype:**
```python
def read_file(filename=""):
    pass
