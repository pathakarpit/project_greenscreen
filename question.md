# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Separate Even and Odd Nodes in a Linked List

**Description:** Given a linked list where each node contains an integer, write a function to separate even nodes from odd nodes while maintaining their original order. The function should return the new linked list with even nodes first, followed by odd nodes.

**Examples:**

1. Input: 0 -> 1 -> 4 -> 6 -> 9 -> 10 -> 11
Output: 0 -> 4 -> 6 -> 10 -> 1 -> 9 -> 11

2. Input: 1 -> 3 -> 5
Output: 1 -> 3 -> 5

3. Input: 2 -> 4 -> 6
Output: 2 -> 4 -> 6

**Constraints:** 
- Each node in the linked list contains a non-negative integer.
- The linked list may be empty (i.e., have no nodes).
- The number of nodes in the linked list is not limited.
- The input linked list is valid (i.e., each node's `next` pointer is either `None` or points to a valid node).
