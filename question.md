# Word Search

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/word-search/](https://leetcode.com/problems/word-search/)

---

## Problem Statement

**Title:** Word Search in a Matrix

**Description:** Given a 2D matrix of characters and a word, determine if the word exists in the matrix by searching for it horizontally or vertically.

```python
# Problem Statement:
# Analyze the given raw content to determine if a word exists in a 2D matrix.
```

**Examples:**

1. **Example 1**
   - Input: `matrix = [["T", "E", "E"], ["S", "G", "K"], ["T", "E", "L"]]`, `word = "GEEK"`
   - Output: `True`
   - Explanation: The word "GEEK" exists in the matrix.
   
2. **Example 2**
   - Input: `matrix = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]`, `word = "ABC"`
   - Output: `True`
   - Explanation: The word "ABC" exists in the matrix.
   
3. **Example 3**
   - Input: `matrix = [["T", "E", "E"], ["S", "G", "K"], ["T", "E", "L"]]`, `word = "NOTFOUND"`
   - Output: `False`
   - Explanation: The word "NOTFOUND" does not exist in the matrix.

**Constraints:** 1 <= N, M <= 100 (matrix size), 1 <= len(word) <= 10.
