# counting sort

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/counting-sort/](https://www.geeksforgeeks.org/counting-sort/)

---

## Problem Statement

**Title:** Counting Sort Algorithm Implementation

**Description:** Given an array of integers within a specific range, implement a counting sort algorithm to efficiently sort the elements.

**Examples:**

1.  Input: [4, 2, 2, 8, 3, 3, 1]
    Output: [1, 2, 2, 3, 3, 4, 8]

2.  Input: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

3.  Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

**Constraints:**

*   The input array consists of integers within the range 0 to max_value.
*   max_value is a constant that represents the maximum value in the input array.
*   The size of the input array (n) is relatively small compared to the maximum value (max).
*   Negative numbers and decimal values are not handled by this implementation.
