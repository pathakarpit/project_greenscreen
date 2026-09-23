# Merge K Sorted Lists

**Difficulty:** Hard  
**Link:** [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## Problem Statement

**Title:** Merging K Sorted Linked Lists
**Description:**
Given k sorted linked lists, merge them into one sorted linked list.
**Examples:**

* Input: 
  List1: 1 -> 3 -> 5 -> 7
  List2: 2 -> 4 -> 6 -> 8
  List3: 0 -> 9 -> 10 -> 11
  
  Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11

* Input:
  List1: 1 -> 3
  List2: 2 -> 4
  List3: 5 -> 7
  
  Output: 1 -> 2 -> 3 -> 4 -> 5 -> 7

* Input:
  List1: 1 -> 3 -> 5
  List2: None
  List3: 0 -> 9
  
  Output: 0 -> 1 -> 3 -> 5 -> 9

**Constraints:** 
- Each linked list is sorted in ascending order.
- The number of linked lists (k) will be a positive integer less than or equal to 10^3.
- Each node in the linked list contains an integer value.
