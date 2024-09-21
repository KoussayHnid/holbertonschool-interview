# Palindrome Integer 💻

## Description 💬
A palindrome integer is a number that remains the same when read forwards or backwards, meaning it's symmetric around its midpoint. For instance, 121, 1221, and 1331 are examples of palindrome integers. To determine if an integer is a palindrome, one can simply reverse its digits and check if the reversed number equals the original. If they match, then the number is a palindrome. Palindrome integers are of interest in various mathematical contexts due to their unique property.

## Tasks 📚

### 0. Palindrome Unsigned Integer
Write a function that checks whether or not a given unsigned integer is a palindrome.

- Prototype: `int is_palindrome(unsigned long n);`
- `n` is the number to be checked.
- Your function must return `1` if `n` is a palindrome, and `0` otherwise.
- You are not allowed to allocate memory dynamically (malloc, calloc, …)

## Example Usage

Compile the program using the provided `main` function in `0-main.c`.

```bash
gcc -Wall -Wextra -Werror -pedantic -g3 -o palindrome 0-main.c 0-is_palindrome.c
