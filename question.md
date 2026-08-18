# Backtracking Set 2 Rat in a Maze

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/](https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/)

---

## Problem Statement

**Title:** Find All Valid Paths in a Binary Matrix Maze


**Description:**

Given a binary matrix maze[][] of size n × n containing values 0 and 1, find all possible paths for a rat to travel from the source cell (0, 0) to the destination cell (n - 1, n - 1). The rat can move in four directions: up, down, left, and right. 1 represents an open cell through which the rat can move. 0 represents a blocked cell that cannot be traversed. The rat can move only through open cells and cannot visit the same cell more than once in a path. Return all valid paths as strings consisting of 'U', 'D', 'L', and 'R', representing the sequence of moves taken by the rat. Note: Return the paths in lexicographically increasing order. If no valid path exists, return an empty list.


**Examples:**


1. Input:
   ```
maze[][] = {{1, 0, 0, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {0, 1, 1, 1}}
```

   Output: 
   ```
["DDRDRR", "DRDDRR"]
```


2. Input:
   ```
maze[][] = {{1, 0}, {0, 1}}
```

   Output:
   ```
[]
```


**Constraints:**


- n × n binary matrix maze
- Each cell contains a value of either 0 or 1
- Source cell is (0, 0)
- Destination cell is (n - 1, n - 1)


### Constraints (continued from above):


- The rat can move in four directions: up, down, left, and right.
- 1 represents an open cell through which the rat can move.
- 0 represents a blocked cell that cannot be traversed.
- The rat can move only through open cells.
- The rat cannot visit the same cell more than once in a path.
