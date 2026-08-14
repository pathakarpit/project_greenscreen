# Median of Stream of Integers Running Integers

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/](https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/)

---

## Problem Statement

**Title:** Maintaining Two Heaps to Find the Median of a Data Stream

**Description:**

Analyze the raw content provided by the Tech Researcher above.


This problem can be solved by maintaining two heaps, one max heap for the smaller half of the elements and another min heap for the larger half.

**Examples:**

1. Input: `addNum(1)` , Output: `0`
2. Input: `addNum(2)` , Output: `0.5`
3. Input: `addNum(3)` , Output: `1`

**Constraints:** 
- The input numbers are integers.
- The two heaps will store the smaller half and larger half of the numbers, respectively.
- If there are an odd number of elements in the data stream, the median is defined as the middle element. Otherwise, it's the average of the two middle elements.

Note: The code implementation provided does not need to be included as part of this problem statement.
