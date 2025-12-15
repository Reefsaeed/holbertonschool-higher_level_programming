# Python - Inheritance

This project covers **inheritance in Python**, including how classes derive from other classes, how attributes/methods are inherited or overridden, and how to inspect objects and class relationships using built-in functions.

## Learning Objectives

By the end of this project, you should be able to explain:

- What a superclass / base class / parent class is
- What a subclass is
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What the default class every class inherits from
- How to override an inherited method or attribute
- Which attributes/methods are inherited by subclasses
- Why inheritance is used
- How and when to use: `isinstance`, `issubclass`, `type`, and `super`

## Requirements

- Language: Python 3.8.5
- OS: Ubuntu 20.04 LTS
- Code style: `pycodestyle` 2.7.*
- All files must be executable
- All files must end with a new line
- First line of each Python file must be:
#!/usr/bin/python3

markdown
Copy code
- A `README.md` is mandatory
- No imports unless explicitly allowed by the task

## Testing

### Run Python files
```bash
./<main_file>.py
Doctest (if tests exist)
All test files are inside the tests/ directory and are executed using:

bash
Copy code
python3 -m doctest ./tests/*
Documentation checks
Examples:

bash
Copy code
python3 -c 'print(__import__("0-lookup").__doc__)'
python3 -c 'print(__import__("0-lookup").lookup.__doc__)'
Files
0-lookup.py
Defines a function lookup(obj) that returns the list of available attributes and methods of an object using built-in introspection.

Prototype:

python
Copy code
def lookup(obj):
    return dir(obj)

Author
Holberton School Student
