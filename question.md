# Group Anagrams

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

---

## Problem Statement

**Title:** Group Anagrams Together
**Description:**
Given a list of words, group anagrams together.
**Examples:**

1. Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Output: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

2. Input: `["abc", "bac", "cab", "bca", "acb", "cba"]`
Output: `[["abc", "bac", "cab", "bca", "acb", "cba"]]`

3. Input: `["listen", "silent", "enlist", "tinsel", "inlets", "telsen", "inlet", "tins", "inle", "silen"]`
Output: `[["listen", "silent", "enlist", "tinsel", "inlets"], ["telsen"], ["inlet"], ["tins"], ["inle", "silen"]]`

**Constraints:** 

* 1 <= N <= 10^5 (where N is the number of words in the input list)
* Each word consists only of lowercase English letters
* The input list may contain multiple anagram groups, and some words might not be part of any anagram group
