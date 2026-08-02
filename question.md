# Searching in an array where adjacent differ by at most k

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/](https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/)

---

## Problem Statement

```
Title: Search Element in Array with Adjacent Difference Constraint
Description: 
Given an array of distinct integers and an integer k, find the first occurrence of x in the array such that the absolute difference between adjacent elements is atmost k. If no such element exists, print "Element not found".

Examples:

1. Input: arr = [2, 4, 5, 7, 7, 6], x = 6, k = 2
Output: Element 6 is present at index 5

2. Input: arr = [2, 4, 5, 7, 7, 6], x = 10, k = 2
Output: Element not found

3. Input: arr = [1, 3, 5, 7, 9], x = 5, k = 3
Output: Element 5 is present at index 2

Constraints:
- The input array contains distinct integers.
- 0 <= k < max(arr[i]) - min(arr[i])
```
