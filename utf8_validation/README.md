-----------------------UTF-8 Validation---------------------------

This project is designed to validate whether a given dataset represents valid UTF-8 encoding. The validation function is implemented in Python and adheres to the requirements of UTF-8 encoding rules.

Requirements:

- **Editor**: vi, vim, emacs
- **OS**: Ubuntu 14.04 LTS
- **Python Version**: Python 3.4.3
- All files should end with a new line.
- The first line of each Python file should be `#!/usr/bin/python3`.
- PEP 8 style guide (version 1.7.x) compliance is mandatory.
- All files must be executable.

Prototype:

```python
def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers representing the dataset.
        
    Returns:
        bool: True if data is valid UTF-8, otherwise False.
    """
