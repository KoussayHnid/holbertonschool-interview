# Sandpiles

## Description

This project involves implementing a function to compute the sum of two sandpiles. Sandpiles are grids of numbers where each cell represents the number of grains of sand. A sandpile is considered stable when none of its cells contains more than 3 grains. If the sum of two sandpiles results in a cell containing more than 3 grains, it becomes unstable and must be toppled, distributing its grains to its neighboring cells. The function must ensure that the resulting sandpile is stable after each toppling round.

## Requirements

- All files are compiled on Ubuntu 14.04 LTS using gcc 4.8.4 with the flags -Wall -Werror -Wextra and -pedantic.
- Each file ends with a new line.
- The code follows the Betty style guidelines and is checked using betty-style.pl and betty-doc.pl.
- Global variables are not allowed.
- No more than 5 functions per file.
- The prototypes of all functions are included in the header file `sandpiles.h`.
- The header file is include-guarded.

## Tasks

### 0. Sandpiles sum

Write a function `sandpiles_sum` that computes the sum of two sandpiles.

- **Prototype:** `void sandpiles_sum(int grid1[3][3], int grid2[3][3]);`
- **Assumption:** Both `grid1` and `grid2` are individually stable.
- When the function is done, `grid1` must be stable.
- `grid1` must be printed before each toppling round, only if it is unstable.

## Compilation and Execution

Example compilation and execution:

```sh
gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-sandpiles.c -o 0-sandpiles
./0-sandpiles
