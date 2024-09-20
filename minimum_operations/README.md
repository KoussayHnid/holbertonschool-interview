# Minimum Operations

## Description

This project involves calculating the minimum number of operations required to achieve exactly `n` 'H' characters in a text file, starting with a single 'H'. The allowed operations are "Copy All" and "Paste". The goal is to determine the fewest number of operations needed to reach the desired number of 'H' characters.

## Requirements

- All files are interpreted/compiled on Ubuntu 14.04 LTS using Python 3.4.3.
- Each file ends with a new line.
- The first line of all files is `#!/usr/bin/python3`.
- A `README.md` file at the root of the project is mandatory.
- Code is documented and follows PEP 8 style guidelines (version 1.7.x).
- All files are executable.

## Task

### 0. Minimum Operations

Write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

- **Prototype:** `def minOperations(n)`
- **Returns:** An integer representing the minimum number of operations.
- **If** `n` **is impossible to achieve, return 0.**

### Example

For `n = 9`:
