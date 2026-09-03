# Backtracking set-8 solving cryptarithmetic puzzles

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/backtracking-set-8-solving-cryptarithmetic-puzzles/](https://www.geeksforgeeks.org/backtracking-set-8-solving-cryptarithmetic-puzzles/)

---

## Problem Statement

**

**Title:** Crypt Arithmetic Puzzle Solver
**Description:**
Given three strings `a`, `b`, and `sum` representing crypt-arithmetic puzzles, solve the puzzle by assigning each letter a unique digit from 0 to 9 such that the arithmetic works out correctly.
**Examples:**
1. Input:
```
a = "send"
b = "more"
sum = "money"
```
Output:
```
7531
0825
08356
```
2. Input:
```
a = "s"
b = "p"
sum = "f"
```
Output:
```
2
1
3
```
3. Input:
```
a = "abc"
b = "def"
sum = "ghi"
```
Output: `-1` (no solution exists)
**Constraints:**

* All input strings contain only lowercase English letters.
* The sum string is the result of adding the first two strings together using standard arithmetic rules.
* Each letter in the input strings must be assigned a unique digit from 0 to 9.
