# Print all the Duplicates in the Input String

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/](https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/)

---

## Problem Statement

```markdown
# Problem Title: Find Duplicates in a String

## Description:
Given a string `s`, find and print all characters that have a frequency greater than 1. This should be done using two methods:

1. Sorting method: Sort the string and then traverse it to find consecutive duplicates.
2. Hashing method: Use an unordered map (or equivalent data structure in other languages) to count the frequency of each character.

## Examples:

### Example 1:
Input: `s = "geeksforgeeks"`
Output:
- Sorting method: `[ ['e', 4], ['f', 2], ['g', 3], ['k', 2], ['o', 1], ['r', 2], ['s', 2] ]`
- Hashing method: `[ ['e', 4], ['f', 2], ['g', 3], ['k', 2], ['r', 2], ['s', 2] ]`

### Example 2:
Input: `s = "aaaabbbbcccc"`
Output (Sorting method):
- `[ ['a', 5], ['b', 4], ['c', 4] ]`
Output (Hashing method): Same as above

### Example 3:
Input: `s = "abcdefg"`
Output (both methods): No duplicates found, output is empty or an indication of no duplicates.

## Constraints: 
- The input string `s` will contain only lowercase English letters.
- The length of the string `s` can be up to 10^5 characters.
```
