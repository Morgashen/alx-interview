#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.

This module provides a function to determine the perimeter of an island
represented in a 2D grid where 1 represents land and 0 represents water.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
grid (List[List[int]]): 2D grid where 1 represents land, 0 represents water.
Each cell is connected horizontally/vertically, not diagonally.

    Returns:
        int: Total perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            # If current cell is land
            if grid[r][c] == 1:
                # Check all 4 adjacent cells (up, down, left, right)
                # Add 1 to perimeter for each water or out-of-bounds cell

                # Up
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1

                # Down
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1

                # Left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1

                # Right
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter


# Optional: Example usage and simple testing
if __name__ == "__main__":
    grid1 = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(island_perimeter(grid1))  # Expected output: 16

    grid2 = [[1]]
    print(island_perimeter(grid2))  # Expected output: 4
