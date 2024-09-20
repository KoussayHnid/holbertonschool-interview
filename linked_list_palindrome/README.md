# Linked List Palindrome

## Description

This project involves implementing a function in C that checks if a singly linked list is a palindrome. A palindrome is a sequence that reads the same forwards and backwards.

## Requirements

- All files are compiled on Ubuntu 14.04 LTS using gcc 4.8.4 with the flags -Wall -Werror -Wextra and -pedantic.
- Each file ends with a new line.
- The code follows the Betty style guidelines and is checked using betty-style.pl and betty-doc.pl.
- Global variables are not allowed.
- No more than 5 functions per file.
- The prototypes of all functions are included in the header file `lists.h`.
- The header file is include-guarded.

## Tasks

### 0. Linked list palindrome

Write a function `is_palindrome` that checks if a singly linked list is a palindrome.

- **Prototype:** `int is_palindrome(listint_t **head);`
- **Return:** 0 if it is not a palindrome, 1 if it is a palindrome.
- An empty list is considered a palindrome.

## Compilation and Execution

Example compilation and execution:

```sh
gcc -Wall -Werror -Wextra -pedantic 0-main.c linked_lists.c 0-is_palindrome.c -o palindrome
./palindrome
