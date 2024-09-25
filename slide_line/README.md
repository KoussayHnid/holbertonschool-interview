---------------------2048 (Single Line) - Slide Line Algorithm--------------

This project implements a sliding and merging algorithm for a single line of integers, simulating the behavior of the 2048 game mechanics.

Requirements:

Editors: vi, vim, emacs
OS: Ubuntu 14.04 LTS
Compiler: gcc 4.8.4
  - Compilation flags: `-Wall -Werror -Wextra -pedantic`
Coding Style 
  - Code must follow the Betty style.
  - No global variables allowed.
  - No more than 5 functions per file.
File Structure:
  - `slide_line.c`: The file containing the function implementation.
  - `slide_line.h`: Header file defining the prototypes and macros.
  - All files must end with a new line and be include guarded.


Prototype:
```c
int slide_line(int *line, size_t size, int direction);
