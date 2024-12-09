#

## Island Perimeter

This project revolves around determining the perimeter of an island represented within a 2D grid. The grid consists of integer values, where 0 signifies water and 1 represents land. The island is connected horizontally and vertically, but not diagonally.

### Problem Description

Our objective is to create a function `island_perimeter(grid)` that calculates the perimeter of the island within the given grid. The function takes the grid as an argument, which is a list of lists of integers.

### Constraints

- The grid is rectangular, with both width and height not exceeding 100.
- The grid is entirely surrounded by water.
- There is only one island (or nothing) within the grid.
- The island does not contain any "lakes" (water bodies not connected to the surrounding water).

### Approach

To solve this problem, we iterate through each cell in the grid using nested loops. We check the value of each cell and its adjacent cells to determine whether it contributes to the island's perimeter. If a cell is surrounded by water on all sides, it contributes 4 to the perimeter. If it has an adjacent water cell, it contributes 3, and so on.

### Required Skills

- Proficiency in algorithms and data structures (specifically 2D arrays)
- Understanding of conditional logic
- Familiarity with counting techniques

### Resources

- [Nested Lists in Python](https://www.w3schools.com/python/python_lists_nested.asp)
- [Multidimensional Arrays in Python](https://www.geeksforgeeks.org/multidimensional-array-in-python/)
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

### Usage

Refer to the `0-main.py` file for an example of how to use the `island_perimeter()` function. Execute the main script using the following command:

```
python3 0-main.py
```

The output will be the perimeter of the island in the provided grid.
