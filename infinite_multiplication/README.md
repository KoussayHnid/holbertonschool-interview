# Infinite Multiplication 💻

## Description 💬
This program multiplies two positive numbers passed as arguments and prints the result.

- Usage: `mul num1 num2`
- `num1` and `num2` will be passed in base 10.
- The result is printed, followed by a new line.
- If the number of arguments is incorrect, it prints "Error" and exits with a status of 98.
- `num1` and `num2` should only be composed of digits. If not, it prints "Error" and exits with a status of 98.
- The program is compiled using the provided `_putchar.c`.

## Tasks 📚

### 0. Infinite Multiplication
Write a program that multiplies two positive numbers:

- Usage: `mul num1 num2`
- `num1` and `num2` will be passed in base 10.
- Print the result, followed by a new line.
- If the number of arguments is incorrect, print "Error", followed by a new line, and exit with a status of 98.
- `num1` and `num2` should only be composed of digits. If not, print "Error", followed by a new line, and exit with a status of 98.

## Example Usage

Compile the program using the provided `_putchar.c`.

```bash
gcc -Wall -pedantic -Werror -Wextra 0-mul.c _putchar.c -o mul
