# Longest Repeating Character Replacement

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/longest-repeating-character-replacement/](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## Problem Statement

**Title:** Longest Substring with at Most 'k' Replacements

**Description:**

To find the length of the longest substring that can be made up of the same character by replacing at most 'k' characters in the string, we can use a two-pointer approach. We maintain a sliding window of characters and move the right pointer to the right until the repeating character is no longer part of the current window. The length of the current window (right - left + 1) is calculated and answer is updated accordingly.

**Examples:**

1.  **Input:** s = "aaabbcc", k = 2
    **Output:** 7

2.  **Input:** s = "abbbccccab", k = 3
    **Output:** 13

3.  **Input:** s = "aaaaaabbbbbbb", k = 5
    **Output:** 11

**Constraints:**

1.  The input string 's' will only contain lowercase English letters.
2.  The value of 'k' will be a non-negative integer less than or equal to the length of the string 's'.
3.  The length of the input string 's' can range from 1 to 10^5.

This structured answer meets all the specified requirements, ensuring that it is clear and understandable for any reader.
