# Linked List Cycle

**Difficulty:** Easy  
**Link:** [https://leetcode.com/problems/linked-list-cycle/](https://leetcode.com/problems/linked-list-cycle/)

---

## Problem Statement

**Title:** Detect Cycle in Linked List

**Description:** Given the head of a singly linked list, determine whether the list contains a cycle. A cycle exists if, while traversing the list through next pointers, you encounter a node that has already been visited instead of eventually reaching nullptr.

**Examples:**

1. Input: head: 1 -> 3 -> 4 -> 3
   Output: true
   Explanation: The last node of the linked list does not point to NULL; instead, it points to an earlier node in the list, creating a cycle.

2. Input: head: 1 -> 8 -> 3 -> 4 -> NULL
   Output: false
   Explanation: The last node of the linked list points to NULL, indicating the end of the list.

3. Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
   Output: true
   Explanation: There is a cycle in the linked list.

**Constraints:** The linked list may have at most 10^5 nodes, and each node's value will be between 1 and 10^9.
