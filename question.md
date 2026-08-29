# Find Shortest Safe Route in a Path with Landmines

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/](https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/)

---

## Problem Statement

```
**Title:** Shortest Safe Route
**Description:**
Given a 2D binary matrix representing a grid with landmines (0) and safe cells (1), find the shortest path from the top-left cell to the bottom-right cell while avoiding landmines. If no such path exists, return "No safe route found".

**Examples:**

* Example 1:
Input: [[1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]]
Output: "10"

* Example 2:
Input: [[1, 0, 0],
        [0, 1, 1],
        [1, 1, 1]]
Output: "No safe route found"

* Example 3:
Input: [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
Output: "10"

**Constraints:**

- The input grid is a square matrix (same number of rows and columns).
- Each cell in the grid contains either a landmine (0) or a safe cell (1).
- The top-left cell and bottom-right cell are guaranteed to be safe cells.
- The maximum size of the grid is 100x100 cells.

```
