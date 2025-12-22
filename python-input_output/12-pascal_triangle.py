#!/usr/bin/python3
"""Generate Pascal's triangle as a list of lists."""


def pascal_triangle(n):
    """Return Pascal's triangle of size n as a list of lists."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
