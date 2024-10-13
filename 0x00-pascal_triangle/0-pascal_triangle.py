#!/usr/bin/python3
""" Pascal Triangle """

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row as [1]

    for i in range(1, n):
        row = [1]  # First element of every row is 1
        for j in range(1, i):
            # The next element is the sum of two elements directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of every row is 1
        triangle.append(row)

    return triangle
