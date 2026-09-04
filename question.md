# Find paths from corner cell to middle cell in maze

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/find-paths-from-corner-cell-to-middle-cell-in-maze/](https://www.geeksforgeeks.org/find-paths-from-corner-cell-to-middle-cell-in-maze/)

---

## Problem Statement

```
Title: Find Paths from Corner Cell to Middle Cell in Maze
Description:
Given an n x n maze represented as a 2D array, where 0 represents an open cell and 1 represents an obstacle, find all paths from the corner cell (top-left) to the middle cell (n/2, n/2).
Input/Output Examples:

Example 1:
Input: n = 3, maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Output: ["DLRU", "DRUL"]

Example 2:
Input: n = 4, maze = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
Output: ["DLRU", "DRUL"]

Constraints:
- n >= 2 (at least a 2x2 maze)
- All cells in the maze are either 0 or 1
```
