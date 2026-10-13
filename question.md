# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Divide Linked List into Even and Odd Nodes

**Description:** Given a singly linked list, write a function to divide it into two separate lists: one containing even nodes and the other containing odd nodes. The even list should be constructed by moving all even nodes from the original list to the result list, while preserving the original order. The odd list will contain the remaining nodes from the original list. If there are no even nodes in the list, return the original list unchanged.

**Examples:**

1. **Example 1:** Input: `17->15->8->9->2->4->6` Output: `8->2->4->6->15->9->17`
2. **Example 2:** Input: `1->3->5->7` Output: `1->3->5->7` (no even nodes)
3. **Example 3:** Input: `2->4->6->8` Output: `2->4->6->8` (all even nodes)

**Constraints:**

*   The linked list is singly linked, meaning each node has a reference to the next node, but not to the previous node.
*   The linked list contains only integers as node values.
*   The input linked list is not empty.
*   The number of nodes in the linked list is less than or equal to 10^5.
