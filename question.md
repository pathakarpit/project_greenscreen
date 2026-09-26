# Sum of two linked lists

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/sum-of-two-linked-lists/](https://www.geeksforgeeks.org/sum-of-two-linked-lists/)

---

## Problem Statement

**Title:** Add Two Linked Lists Using Recursion

**Description:**

Given two singly linked lists representing numbers in base 10, add them together and return the resulting linked list. The input linked lists may contain leading zeros.

**Examples:**

*   **Example 1:** Input: `num1 = 123` (represented as `1 -> 2 -> 3`) and `num2 = 999` (represented as `9 -> 9 -> 9`). Output: `1222` (represented as `1 -> 2 -> 2 -> 2`)
*   **Example 2:** Input: `num1 = 456` (represented as `4 -> 5 -> 6`) and `num2 = 0` (represented as `->`). Output: `456` (represented as `4 -> 5 -> 6`)
*   **Example 3:** Input: `num1 = 0` (represented as `->`) and `num2 = 999` (represented as `9 -> 9 -> 9`). Output: `999` (represented as `9 -> 9 -> 9`)

**Constraints:**

*   The input linked lists only contain single-digit nodes.
*   The maximum value that can be stored in a node is 9.
*   The length of the input linked lists is at most 1000.

### Note:
This problem requires you to implement a function that takes two singly linked lists as input and returns their sum as another linked list. You should use recursion to solve this problem, as indicated by the presence of recursive functions in the provided code snippets. Additionally, please ensure that your solution handles edge cases such as linked lists with leading zeros or empty linked lists.
