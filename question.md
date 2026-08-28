# Print all Palindromic Partitions of a String

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/print-palindromic-partitions-string/](https://www.geeksforgeeks.org/print-palindromic-partitions-string/)

---

## Problem Statement

Title: Palindrome Partitioning
Description: The function `palinParts` generates all possible partitions of the input string such that each substring in the partition is a palindrome. It uses recursion with backtracking to explore all possible combinations.
Examples:
1. Input: "geeks"
Output:
[
  ["g", "e", "e", "k", "s"],
  ["g", "ee", "k", "s"]
]
2. Input: "abba"
Output:
[
  ["a", "b", "b", "a"],
  ["a", "bb", "a"],
  ["abba"]
]
3. Input: "aaa"
Output:
[
  ["a", "a", "a"],
  ["aa", "a"],
  ["aaa"]
]
Constraints:
- The input string is a non-empty string of lowercase English letters.
- The length of the input string is between 1 and 10^5 (inclusive).
- Each substring in the partition must be at least one character long.
