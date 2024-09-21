# Linked List Cycle

## Overview

This project involves implementing a function in C that checks if a singly linked list has a cycle in it.

## Requirements

- **Allowed Editors:** vi, vim, emacs
- **Compilation Environment:** Ubuntu 14.04 LTS
- **Compiler:** gcc 4.8.4 with flags `-Wall -Werror -Wextra -pedantic`
- **Functions Allowed:** `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
- **No Usage of Global Variables**
- **Maximum Functions per File:** 5
- **Header File:** `lists.h` containing structure definition and function prototypes
- **Header Files Include Guarded**

## File Structure

- **lists.h:** Header file containing structure definition and function prototypes.
- **0-linked_lists.c:** Utility functions to work with singly linked lists.
- **0-main.c:** Main function used for testing the `check_cycle` function.
- **0-check_cycle.c:** Implementation of the `check_cycle` function.

## Usage

1. Compile the project using:

```bash
gcc -Wall -Werror -Wextra -pedantic 0-main.c 0-check_cycle.c 0-linked_lists.c -o cycle
