# Set Matrix Zeroes

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/set-matrix-zeroes/](https://leetcode.com/problems/set-matrix-zeroes/)

---

## Problem Statement

**Title:** Modify Matrix with Zero Rows and Columns


**Description:** You are given a 2D matrix mat[][] of size n x m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0.


### Examples:

*   **Example 1:**
    *   **Input:** 
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
    *   **Output:** 
        [[1,0,1],
         [0,0,0],
         [1,0,1]]

*   **Example 2:**
    *   **Input:** 
        [[0,1,2,0],
         [3,4,5,2],
         [1,3,1,5]]
    *   **Output:** 
        [[0,0,0,0],
         [0,4,5,0],
         [0,3,0,0]]


### Constraints:
- The input matrix will only contain 0 and positive integers.
