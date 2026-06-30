# Boyer Moore Algorithm for Pattern Searching

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/](https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/)

---

## Problem Statement

Title: Boyer Moore Algorithm for Pattern Searching - GeeksforGeeks
Description:

The Boyer Moore Algorithm is a string searching algorithm that uses two main ideas to find the first occurrence of a pattern in a given text.

Input/Output Examples:


1. 
Input: txt = "ABAAABCD", pat = "ABC"
Output: 0


2.
Input: txt = "ABCDABD", pat = "ABD"
Output: 0, 3


3.
Input: txt = "ABCDABCD", pat = "ABC"
Output: 0, 4


Constraints:


* The input text (txt) and pattern (pat) are strings of characters, where each character is either a lowercase letter or an uppercase letter.


* The length of the pattern (m) must be less than the length of the text (n).
