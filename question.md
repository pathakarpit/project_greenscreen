# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Segregate even and odd nodes in a Linked List

**Description:** Given a singly linked list, rearrange the list in place so that all nodes containing even values appear before nodes containing odd values. Return the head of the modified linked list. Note: The relative order of the even nodes and the odd nodes should remain unchanged.

**Examples:**

1. **Input:** 8 -> 2 -> 4 -> 6 -> 17 -> 15 -> 9
**Output:** 8 -> 2 -> 4 -> 6 -> 17 -> 15 -> 9
**Explanation:** Since 8, 2, 4, and 6 are even, they appear first in the list, followed by the odd numbers 17, 15, and 9.

2. **Input:** 1 -> 3 -> 5 -> 7
**Output:** 1 -> 3 -> 5 -> 7
**Explanation:** There are no even numbers in the list.

3. **Input:** 2 -> 4 -> 6 -> 8 -> 10
**Output:** 2 -> 4 -> 6 -> 8 -> 10
**Explanation:** All numbers in the list are even, so they appear in the same order.

**Constraints:** 
- The linked list is a singly linked list.
- The nodes in the linked list contain integer values.
- The relative order of the even nodes and the odd nodes should remain unchanged.

Note: The solution involves traversing the linked list once and maintaining two separate lists for even and odd nodes. The even list is appended to the odd list at the end to obtain the modified linked list.
