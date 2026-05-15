# Wildcard String Matching

**Difficulty:** Medium  
**Link:** [https://practice.geeksforgeeks.org/problems/wildcard-string-matching1126/1](https://practice.geeksforgeeks.org/problems/wildcard-string-matching1126/1)

---

## Problem Statement

**Title:** Recursive Wild Card Pattern Matching
**Description:**

Analyze the raw content provided by the Tech Researcher above.


```
Given two strings `text` and `pattern`, determine if `pattern` matches `text` using wildcards (`*`) for any number of characters.

Core Problem Statement:

Given a string `text` and a pattern `pattern`, return True if the pattern matches the text, False otherwise.

Input/Output Examples:

1. Input: `text = "abcde", pattern = "a?c*"`
   Output: `True`

2. Input: `text = "abcde", pattern = "abcdefg"`
   Output: `False`

3. Input: `text = "abcde", pattern = "*"`
   Output: `True`


Constraints:

- 1 <= len(text) <= 100
- 1 <= len(pattern) <= 100

```
Note that the constraints are added to limit the input size and prevent excessive computation.
