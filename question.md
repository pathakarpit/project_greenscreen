# Create a Matrix with Alternating Rectangles of O and X

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/create-a-matrix-with-alternating-rectangles-of-0-and-x/](https://www.geeksforgeeks.org/create-a-matrix-with-alternating-rectangles-of-0-and-x/)

---

## Problem Statement

Title: Create a matrix with alternating rectangles of O and X

Description:
Write a code which inputs two numbers m and n and creates a matrix of size m x n (m rows and n columns) in which every elements is either X or 0. The Xs and 0s must be filled alternatively, the matrix should have outermost rectangle of Xs, then a rectangle of 0s, then a rectangle of Xs, and so on.

Examples:
Input: m = 3, n = 3

Output:
X X X
X 0 X
X X X


Input: m = 4, n = 5

Output:
X X X X X
X 0 0 0 X
X 0 0 0 X
X X X X X


Input: m = 5, n = 5

Output:
X X X X X
X 0 0 0 X
X 0 X 0 X
X 0 0 0 X
X X X X X


Input: m = 6, n = 7

Output:
X X X X X X X
X 0 0 0 0 0 X
X 0 X X X 0 X
X 0 X X X 0 X
X 0 0 0 0 0 X
X X X X X X X

Constraints: 
1 ≤ m, n ≤ 10^5
