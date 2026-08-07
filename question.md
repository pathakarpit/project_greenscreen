# Find Duplicates in O(n) Time and O(1) Extra Space

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/](https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/)

---

## Problem Statement

**Title:** 
Find the Pair of Integers with the Smallest Absolute Difference


**Description:**
Given an array nums of distinct integers, find all pairs of indices (i and j) such that nums[i] + nums[j] equals the target value sum. The pair should include a number from each end, i.e., index i must be less than or equal to index j.

Return all possible pairs with their indices in the array, note that the same pair could appear multiple times but it will always have two different indices.


**Examples:**

1.
Input: nums = [2, 7, 11, 15], target = 9
Output: [[0,1],[1,0]]

2.
Input: nums = [10,20,3,40], target = 33
Output: [[0,1],[1,0]]

3.
Input: nums = [1,2,3,4,5], target = 7
Output: [[0,1]]


**Constraints:**
1 <= len(nums) <= 10^5
-10^9 <= nums[i] <= 10^9
-10^9 <= sum <= 10^9
