# Soduko

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/backtracking-set-7-suduku/](https://www.geeksforgeeks.org/backtracking-set-7-suduku/)

---

## Problem Statement

**Sudoku**
================

**Description:**
Given a 9x9 Sudoku board as a 2D array of integers, fill in all the empty cells (0) with valid numbers from 1 to 9 such that no row, column, or 3x3 sub-grid contains more than one instance of each number.

**Examples:**

* Input:
```
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
```
Output:
```
grid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],

        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],

        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
```
**Constraints:**

* The input grid is a 9x9 2D array of integers.
* Each row, column, and 3x3 sub-grid can contain each number from 1 to 9 only once.
