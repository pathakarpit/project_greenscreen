# Solve the Sudoku

**Difficulty:** Medium  
**Link:** [https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1](https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1)

---

## Problem Statement

**Sudoku Problem**
================

### Description
------------

Given an incomplete Sudoku configuration in terms of a 9 x 9 2-D square matrix (grid[][]), the task is to find a solved Sudoku. For simplicity, you may assume that there will be only one unique solution.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Zeros in the grid indicates blanks, which are to be filled with some number between 1-9. You cannot replace the element in the cell which is not blank.

Iterate over the grid and look for positions which have not been filled. If position pos is 0, it means it has not been filled yet. We can try filling it with values [1, 9] one by one iff it is valid. Let’s say we want to check if 1 can be filled. So, we verify if there is no row which already has 1, no column already has 1 and that corresponding 3x3 sub square does not have one. If it is possible, then we put one and move to the next position recursively. If we have covered all positions, that means we found a valid sudoku grid. Otherwise, it will keep backtracking until all options are exhausted.

### Examples
----------

#### Example 1

Input:
```
grid = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]
```

Output:
```
grid = [
[5,3,4,6,7,8,9,1,2],
[6,7,2,1,9,5,3,4,8],
[1,9,8,3,4,2,5,6,7],
[8,5,9,7,6,1,4,2,3],
[4,2,6,8,5,3,7,9,1],
[7,1,3,9,2,4,8,5,6],
[9,6,1,5,3,7,2,8,4],
[2,8,7,4,1,9,6,3,5],
[3,4,5,2,8,6,1,7,9]
]
```

#### Example 2

Input:
```
grid = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]
```

Output:
```
grid = [
[5,3,4,6,7,8,9,1,2],
[6,7,2,1,9,5,3,4,8],
[1,9,8,3,4,2,5,6,7],
[8,5,9,7,6,1,4,2,3],
[4,2,6,8,5,3,7,9,1],
[7,1,3,9,2,4,8,5,6],
[9,6,1,5,3,7,2,8,4],
[2,8,7,4,1,9,6,3,5],
[3,4,5,2,8,6,1,7,9]
]
```

#### Example 3

Input:
```
grid = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]
```

Output:
```
grid = [
[5,3,4,6,7,8,9,1,2],
[6,7,2,1,9,5,3,4,8],
[1,9,8,3,4,2,5,6,7],
[8,5,9,7,6,1,4,2,3],
[4,2,6,8,5,3,7,9,1],
[7,1,3,9,2,4,8,5,6],
[9,6,1,5,3,7,2,8,4],
[2,8,7,4,1,9,6,3,5],
[3,4,5,2,8,6,1,7,9]
]
```

### Constraints
------------

*   The input grid will be a 9 x 9 2-D square matrix.
*   Each cell in the grid can contain a number between 0 and 9, inclusive. A value of 0 indicates an empty cell.
*   There will be exactly one unique solution to each Sudoku puzzle.

Note: The constraints are inferred from the problem description and examples provided. They may need to be adjusted based on specific requirements or edge cases.
