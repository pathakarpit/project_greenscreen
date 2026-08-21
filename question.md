# Longest Possible Route in a Matrix with Hurdles

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/](https://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/)

---

## Problem Statement

```
Title: Longest Path in Matrix using Depth-First Search
Description: Given a matrix `mat` and two cells `(xs, ys)` and `(xd, yd)`, find the length of the longest path from `(xs, ys)` to `(xd, yd)` using depth-first search with backtracking.
Examples:
1. Input: mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], xs = 0, ys = 0, xd = 2, yd = 2
Output: 3 (path: [(0, 0), (1, 0), (2, 2)])

2. Input: mat = [[1, 1], [1, 1]], xs = 0, ys = 0, xd = 1, yd = 1
Output: 1 (path: [(0, 0), (1, 1)])

3. Input: mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], xs = 2, ys = 2, xd = 0, yd = 0
Output: -1 (no path from `(2, 2)` to `(0, 0)` due to blocked cell at `(0, 0)`)
Constraints:
- Matrix `mat` is a square matrix with dimensions up to `10^5`.
- Cells `(xs, ys)` and `(xd, yd)` are within the bounds of the matrix.
- The value of each cell in `mat` is either `1` (path can be traversed) or `0` (blocked).
```
