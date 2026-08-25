# Knight Tour

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/](https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/)

---

## Problem Statement

**Title:** Knight's Tour Problem


**Description:** 

Given an 8x8 chessboard, find a path for a knight to visit each square exactly once and return to the starting point. The knight moves according to certain rules: it can move two squares horizontally then one vertically or vice versa.

The problem is related to graph theory and can be solved using various algorithms and heuristics.


**Examples:** 

1. 
Start at square (0, 0)
Visit each square exactly once
Return to the starting point


2. 
Start at square (4, 4)
Move to square (6, 5) 
Then visit each remaining square in some order
End up back on square (4, 4)


3. 
Start at square (1, 1)
Visit squares in the following order: (3, 2), (5, 3), (7, 2), (5, 1), (3, 0), (1, 2), (0, 0)
This is just one possible solution


**Constraints:** 

* The chessboard is an 8x8 grid.
* The knight moves according to the standard rules: two squares horizontally then one vertically or vice versa.
* Each square can only be visited once.
* The path must end up back on the starting point.
