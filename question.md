# Given a Matrix of ‘O’ and ‘X’, Replace ‘O’ with ‘X’ if Surrounded by ‘X’

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/](https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/)

---

## Problem Statement

**

**Title:** Marking Islands in a 2D Grid

**Description:** Given an m x n grid where each cell is either 'O' (representing an island) or 'X' (representing water), write a function to mark all connected islands as 'T' and the rest of the grid as 'X'. The function should modify the input grid in-place.

**Examples:**

1. Input:
```python
board = [
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"]
]
```

Output:
```python
board = [
    ["T", "T", "T", "T"],
    ["T", "T", "T", "T"],
    ["T", "T", "T", "T"]
]
```
2. Input:
```python
board = [
    ["X", "O", "O", "X"],
    ["X", "O", "X", "X"],
    ["X", "X", "X", "X"]
]
```

Output:
```python
board = [
    ["T", "T", "T", "T"],
    ["T", "T", "T", "T"],
    ["T", "T", "T", "T"]
]
```
3. Input:
```python
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
```

Output:
```python
board = [
    ["T", "T", "T", "T"],
    ["T", "T", "T", "T"],
    ["T", "T", "T", "T"],
    ["T", "T", "T", "T"]
]
```
**Constraints:** The grid is represented as a 2D list of size m x n, where each cell is either 'O' or 'X'. The function should modify the input grid in-place.
