# Trapping Rain Water

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

---

## Problem Statement

**Container With Most Water**

**Description:** Given an array of heights, find the maximum amount of water that can be trapped between bars in an array.

```
Examples:

Example 1:
Input: heights = [2, 0, 1]
Output: 1
Explanation: The area of water held between the bars at indices 1 and 0 is 1 unit, which is the maximum area we can trap.

Example 2:
Input: heights = [3, 1, 4, 6, 7, 5, 2]
Output: 12
Explanation: The area of water held between the bars at indices 3 and 4 is 2 units, and between the bars at indices 4 and 5 is 1 unit. So the maximum area we can trap is 12 units.

Example 3:
Input: heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
```

**Constraints:** 
- The input array `heights` will contain non-negative integers.
- The number of elements in the array `heights` can range from 1 to 10^6.
- The maximum value that each element in the array `heights` can hold is 10^5.
