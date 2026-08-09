# Product of Array except itself

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/a-product-array-puzzle/](https://www.geeksforgeeks.org/a-product-array-puzzle/)

---

## Problem Statement

```
Title: Find the product of all numbers in an array except for each number itself.
Description:
Given an array of integers, calculate the product of all elements except for each element at its respective index. The product should be calculated as follows:

- For the first element (at index 0), consider only the second element (at index 1). So, the result for the first element will be `arr[1]`.
- For the last element (at index N-1), consider all elements before it except itself. So, the result for the last element will be product of all elements from the start to `(N-2)`th index.
- For each other element in between, consider both the elements preceding and succeeding it.

Examples:

1. Input: `[10, 3, 5, 6, 2]`
   Output: `[(3*5*6*2), (10*5*6*2), (10*3*6*2), (10*3*5*2)]` which is equivalent to `[180, 600, 60, 150]`

2. Input: `[1, 2, 3, 4]`
   Output: `[(2*3*4), (1*3*4), (1*2*4), (1*2*3)]` which is equivalent to `[24, 12, 8, 6]`

3. Input: `[5, 10, -1, 7]`
   Output: `[(10*-1*7), (5*-1*7), (5*10*7), (5*10*-1)]` which is equivalent to `[-70, -35, 350, -50]`

Constraints:
- The array length will be at least 2.
- Array elements can be negative integers or zero.

```
