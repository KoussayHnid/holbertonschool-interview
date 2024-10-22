#!/usr/bin/python3
"""
perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Check for adjacent land cells and adjust perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    # Remove 2 sides (shared edge) for land above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Remove 2 sides (shared edge) for land to the left
                    perimeter -= 2

    return perimeter
