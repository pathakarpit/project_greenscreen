# Make all Array Elements Equal

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/make-array-elements-equal-minimum-cost/](https://www.geeksforgeeks.org/make-array-elements-equal-minimum-cost/)

---

## Problem Statement

**Title:** Binary GCD Algorithm Time Complexity Analysis

**Description:**

The time complexity of the binary GCD algorithm is O(n^2) for arbitrarily large numbers and O(n* log_2(n)) when working with word-sized numbers, where n represents the number of bits in the larger of the two input numbers. This makes it comparable to the Euclidean algorithm's time complexity under certain conditions.

**Examples:**

1. Input: Two arbitrarily large integers (e.g., 10^100 and 5*10^20)  
Output: Time complexity is O(n^2), where n is the number of bits in the larger integer.
2. Input: Two word-sized numbers (e.g., 32-bit integers) with values close to their maximum limit.  
Output: Time complexity is O(n* log_2(n)), where n is the number of bits in the larger integer.
3. Input: Two large numbers with a small difference between them (e.g., 10^100 and 10^100 + 1).  
Output: Time complexity remains O(n^2) due to the algorithm's nature.

**Constraints:** 

- The input integers are arbitrarily large or word-sized.
- n represents the number of bits in the larger integer.
- No constraints on the range or magnitude of the input numbers, except for those mentioned above.
