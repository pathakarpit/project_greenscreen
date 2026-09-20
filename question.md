# Delete nodes which have a greater value on right side

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/](https://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/)

---

## Problem Statement

```
Title: Delete Nodes from Right Side of Linked List
Description:
Given a linked list where each node contains an integer value, remove all nodes that have a greater value than their next node. If a node's value is less than its next node's value, it should remain in the list.

Examples:
Example 1:
Input: 12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3
Output: 2 -> 3

Example 2:
Input: 4 -> 3 -> 2 -> 1
Output: Empty linked list (all nodes were removed)

Example 3:
Input: 10 -> 20 -> 30 -> 40
Output: 10

Constraints:
- The input linked list will contain at most 1000 nodes.
- All node values are within the range of 0 to 1000000.
```
