# Permute Two Arrays such that Sum of Every Pair is Greater or Equal to K

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/permute-two-arrays-sum-every-pair-greater-equal-k/](https://www.geeksforgeeks.org/permute-two-arrays-sum-every-pair-greater-equal-k/)

---

## Problem Statement

**Title:** Is Possible Pair Sum

**Description:**

Given two arrays `a` and `b`, determine if every pair of elements from these arrays sums to at least `k`. The arrays are not necessarily the same length, but they will have the same number of elements as each other. If it is possible for all pairs to sum to at least `k`, return true; otherwise, return false.

**Examples:**

* Input: `a = [2, 1, 3]`, `b = [7, 8, 9]`, `k = 10` Output: True
* Input: `a = [2, 4, 6]`, `b = [3, 5, 7]`, `k = 11` Output: False
* Input: `a = [1, 2, 3]`, `b = [10, 20, 30]`, `k = 5` Output: True

**Constraints:**

* The length of arrays `a` and `b` will be equal.
* All elements in arrays `a` and `b` will be non-negative integers.
* The value of `k` will be greater than or equal to the maximum element in either array.
