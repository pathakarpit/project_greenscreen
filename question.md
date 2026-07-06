# Find the Number of Islands | Set 1 (Using DFS)

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/find-number-of-islands/](https://www.geeksforgeeks.org/find-number-of-islands/)

---

## Problem Statement

**

```plaintext
Title: Island Counting in Grid

Description:
Given an m x n grid where each cell is either 'W' (Water) or 'L' (Land), count the number of islands. An island is formed by connecting adjacent lands horizontally, vertically, or diagonally.

Examples:

1. Example 1
    - Input: [['L', 'E', 'W', 'W'], ['L', 'R', 'R', 'W'], ['L', 'W', 'R', 'W']]
    - Output: 2

2. Example 2
    - Input: [['L', 'L', 'L'], ['L', 'L', 'L'], ['L', 'L', 'L']]
    - Output: 1

3. Example 3
    - Input: [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
    - Output: 0

Constraints:
- The grid is a rectangular m x n matrix where m and n are positive integers.
- Each cell in the grid contains either 'L' (Land) or 'W' (Water).
- Island formation is restricted to horizontal, vertical, or diagonal connections between lands.
```
