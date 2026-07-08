# Find a Common Element in all Rows of a Given Row-Wise Sorted Matrix

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/find-common-element-rows-row-wise-sorted-matrix/](https://www.geeksforgeeks.org/find-common-element-rows-row-wise-sorted-matrix/)

---

## Problem Statement

```
Title: Find Common Element in All Rows of a Given Row-Wise Sorted Matrix
Description: Given a matrix, the task is to find an element that exists in every row of the given matrix. The matrix is sorted in a specific way, with each element being greater than or equal to the previous one in the same row.
Examples:
Input 1: 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output 1: -1
Explanation 1: There is no common element in the given matrix.

Input 2:
matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
Output 2: 1
Explanation 2: The common element present in every row of the given matrix is 1.

Input 3:
matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
Output 3: -1
Explanation 3: There is no common element in the given matrix.

Constraints: 
1 ≤ m, n ≤ 200 (where m and n are the number of rows and columns in the matrix)
m * n <= 104
```
