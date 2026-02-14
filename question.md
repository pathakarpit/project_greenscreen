# Kth - Smallest Element

**Difficulty:** Medium  
**Link:** [https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1](https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1)

---

## Problem Statement

**Problem Statement:**
Find the kth smallest element in an unsorted array of integers.

**Description:**
Given an array of integers and an integer k, find the kth smallest element in the array. The solution involves using a Max Heap data structure to efficiently select the kth smallest element.


**Examples:**

1. **Input:** arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
   **Output:** The 4th smallest element in the array is 6.

2. **Input:** arr = [1, 2, 3, 4, 5], k = 3
   **Output:** The 3rd smallest element in the array is 3.

3. **Input:** arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], k = 5
   **Output:** The 5th smallest element in the array is 5.


**Constraints:**
- The input array contains n integers.
- The integer k is within the range 1 <= k <= n.
- All elements in the array are distinct positive integers.
