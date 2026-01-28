# Next Permutation

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/next-permutation/](https://leetcode.com/problems/next-permutation/)

---

## Problem Statement

**Title:** Generate Permutations and Next Lexicographic Permutation

**Description:**
Given an array of elements, generate all permutations in lexicographic order. Also, find the next permutation in lexicographic order given a current permutation.

1. Sort the array.
2. Use backtracking to swap elements at different positions for generating permutations.
3. Generate duplicate-safe permutations by sorting the array and skipping repeated choices.

For finding the next permutation:

*   Find the rightmost element that is smaller than its successor (the first pivot).
*   Swap the pivot with the smallest element greater than it on the right side (successor).
*   Reverse all elements on the right side of the pivot to get the next smallest lexicographic permutation.

**Examples:**

1. Input: `arr = [1, 2, 3]`
Output: Permutations in lexicographic order:
`[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

Next Lexicographic Permutation: Given `[1, 2, 3]`, the next permutation is `[1, 3, 2]`.

2. Input: `arr = [3, 2, 1]`
Output: The next lexicographic permutation is not possible because there are no smaller elements on the right side of the pivot.

**Constraints:**

*   The input array will contain integers.
*   The length of the input array can be up to 10^5.
*   The numbers in the array can range from 1 to 10^5.
*   No duplicate values are allowed in the array.
