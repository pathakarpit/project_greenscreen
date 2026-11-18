# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Move Even Nodes to Front of Linked List

**Description:** 

Given a singly-linked list where each node contains an integer, move all even nodes to the front of the list while maintaining their original order relative to each other. The odd nodes should remain in their original order, but appear after all even nodes in the modified list.

**Examples:**

1. **Example 1:**

Original Linked List: `0 -> 1 -> 2 -> 3 -> 4`
Modified Linked List: `0 -> 2 -> 4 -> 1 -> 3`

2. **Example 2:**

Original Linked List: `1 -> 3 -> 5 -> 7 -> 9`
Modified Linked List: `1 -> 3 -> 5 -> 7 -> 9`

3. **Example 3:**

Original Linked List: `0 -> 2 -> 4 -> 6 -> 8`
Modified Linked List: `0 -> 2 -> 4 -> 6 -> 8`

**Constraints:**

* Each node in the linked list contains a non-negative integer.
* The linked list may be empty (i.e., the head is `NULL`).
* The number of nodes in the linked list is limited only by the available memory.

Note: The `moveEvenToFront` function assumes that the input linked list is a singly-linked list where each node contains an integer. It also assumes that the linked list is not empty and that each node has a valid `data` field.
