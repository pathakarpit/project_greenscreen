# Printing all solutions in N-Queen Problem

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/](https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/)

---

## Problem Statement

```
Title: The N Queen Problem
Description: 
The N Queen problem is a classic problem in computer science and mathematics. The goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal.

Examples:
Input: n = 4
Output:
```
[[2, 4, 1, 3], [3, 1, 4, 2]]
```

Explanation: We mainly print column numbers (from first to last row) of every possible configuration.

Input: n = 3
Output: []
Explanation: There are no possible solutions for n = 3

Input: n = 5
Output:
```
[[4, 1, 3, 2, 0], [2, 3, 5, 1, 4]]
```

Explanation: We mainly print column numbers (from first to last row) of every possible configuration.

Constraints:
The input is an integer N representing the size of the chessboard. The output is a list of lists, where each sublist represents a valid placement of queens on the board.
1 <= N <= 10^5
Note: This problem can be solved using backtracking or other algorithms.
```
