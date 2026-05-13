# Count Palindromic Subsequences

**Difficulty:** Medium  
**Link:** [https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1](https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1)

---

## Problem Statement

```
Title: Count Palindromic Subsequences
Description:
Given a string s, return the count of distinct palindromic subsequences in it.
A palindromic subsequence is a sequence that can be formed by deleting some characters from s such that it remains the same when reversed.

Examples:

Example 1:
Input: s = "aab"
Output: 8
Explanation: The possible palindromic subsequences are: 
- a (delete b)
- a (delete b)
- aa (no deletion needed)
- ab (delete a in second occurrence of 'a')
- ba (delete a in first occurrence of 'a')
- bb (no deletion needed)
- aba (delete b)
- abb (delete a)

Example 2:
Input: s = "abc"
Output: 3
Explanation: The possible palindromic subsequences are: 
- a (delete b and c)
- b (delete a and c)
- c (delete a and b)

Example 3:
Input: s = "aaa"
Output: 4
Explanation: The possible palindromic subsequences are: 
- a (no deletion needed)
- aa (no deletion needed)
- aaa (no deletion needed)
- empty string

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters
```
