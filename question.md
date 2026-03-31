# Print all Possible Combinations of r Elements in a Given Array of Size n

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/](https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/)

---

## Problem Statement

```
Title: Generate All Combinations of Size r in an Array

Description:
Given an array `arr` and an integer `r`, write a function to generate all combinations of size `r` from the input array. The combinations should be returned as a list of lists, where each inner list represents a combination.

Examples:

* Input: `arr = [1, 2, 3]`, `r = 2`
Output:
[
  [1, 2],
  [1, 3],
  [2, 3]
]

* Input: `arr = [1, 2, 3, 4]`, `r = 3`
Output:
[
  [1, 2, 3],
  [1, 2, 4],
  [1, 3, 4],
  [2, 3, 4]
]

* Input: `arr = [5, 6, 7, 8]`, `r = 2`
Output:
[
  [5, 6],
  [5, 7],
  [5, 8],
  [6, 7],
  [6, 8],
  [7, 8]
]

Constraints:
1 <= |arr| <= 10^3 (array size)
1 <= r <= min(|arr|, 10) (combination size)
```
