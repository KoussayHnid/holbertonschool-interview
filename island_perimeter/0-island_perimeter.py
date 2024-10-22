#!/usr/bin/python3
"""
perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    grid is a list of lists where:
        - 0 represents water
        - 1 represents land
        - Cells are connected horizontally or vertically.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2  
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2  

    return perimeter