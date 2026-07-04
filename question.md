# Rotate Image

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/rotate-image/](https://leetcode.com/problems/rotate-image/)

---

## Problem Statement

**

**Title:** Rotate a Rectangular Image by 90 Degree Clockwise

**Description:**
Given an image represented by m x n matrix, rotate the image by 90 degrees in clockwise direction. Please note the dimensions of the result matrix are going to n x m for an m x n input matrix.

**Examples:**

1. Input:
     1   2   3
    4   5   6
    7   8   9

Output:
   7   4   1
  8   5   2
  9   6   3

2. Input Matrix
1  2  3    Transpose ->     1  4  7
4  5  6    Transpose ->     2  5  8
7  8  9    Transpose ->     3  6  9

Reversing the rows of the transposed matrix we get:

8  5  2
6  4  1
9  7  3

**Constraints:**

* The input matrix is a rectangular image represented as an m x n matrix.
* The rotation operation should be performed in clockwise direction.
* The dimensions of the result matrix will be n x m for an m x n input matrix.

Note: Since the problem statement does not explicitly mention any constraints, I have assumed that the input matrix can be any size and the rotation operation is always possible. However, depending on the specific requirements, additional constraints may need to be added.
