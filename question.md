# Smallest Window in a String Containing all the Characters of Another String

**Difficulty:** Medium  
**Link:** [https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1](https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1)

---

## Problem Statement

**Title:** Smallest Window Containing All Characters


**Description:** 
Find the smallest window in a string `s1` that contains all characters of another string `s2`. A character is considered present in the window if its frequency in the window is greater than or equal to its frequency in `s2`.

**Examples:**

* Input: `s1 = "ADOBECODEBANC"`, `s2 = "ABC"`
Output: `"BANC"`

* Input: `s1 = "a"`, `s2 = "aa"`
Output: `""`

* Input: `s1 = "bba", s2 = "ab"`
Output: `"bba"`


**Constraints:** 
1. The input strings `s1` and `s2` consist only of lowercase English letters.
2. 1 <= length(s1) <= 10^5
3. 0 <= length(s2) <= 10^4
