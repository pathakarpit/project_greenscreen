# Rabin-Karp Algorithm for Pattern Searching

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/](https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/)

---

## Problem Statement

```
Title: Rabin-Karp Algorithm Pattern Search

Description:
Given a text string T of length N and a pattern string P of length M, implement the Rabin-Karp algorithm to efficiently detect all occurrences of P in T. The algorithm should use rolling hash functions to compute the hash value of a string starting at each position of T with the same length as P.

Examples:

1. Input: 
   T = "banana"
   P = "ana"
   
   Output:
   Positions of pattern occurrence: [1, 3]

2. Input: 
   T = "abcdefg"
   P = "cde"

   Output:
   Positions of pattern occurrence: [2]

3. Input: 
   T = "abracadabra"
   P = "abra"

   Output:
   Positions of pattern occurrence: [0, 7]

Constraints:
1 <= N, M <= 10^6
All characters in both T and P are lowercase English letters.

Note: The algorithm should be able to handle multiple patterns and return all occurrences.
```
I hope this meets the requirements!
