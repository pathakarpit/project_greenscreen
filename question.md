# Given an Array of Numbers Arrange the Numbers to Form the Biggest Number

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/](https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/)

---

## Problem Statement

**Title:** Largest Concatenated Number

**Description:** 
Given a list of strings representing numbers in string format, find the largest number that can be formed by concatenating these strings.

Remove any non-digit characters from each string and sort all the remaining digits in descending order (from largest to smallest). If there is a tie, we compare the first digit to break it. The resulting sorted string will represent the largest concatenated number.

**Examples:**

1. Input: ["2", "21", "12"]
   Output: "1212"
   Explanation: The largest concatenated number formed by these strings is 1212.
   
2. Input: ["3", "30", "33"]
   Output: "3330"
   Explanation: The largest concatenated number formed by these strings is 3330.

3. Input: ["1", "11", "13"]
   Output: "31113"
   Explanation: The largest concatenated number formed by these strings is 31113.

**Constraints:** 
* N <= 10^5 (where N is the maximum length of any string in the input list).
* All numbers in the input list are non-negative.
* No leading zeroes will be present in the output.
