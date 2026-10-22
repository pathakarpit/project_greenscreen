# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Segregate even and odd nodes in a Linked List

**Description:** Given a singly linked list, rearrange the list in place so that all nodes containing even values appear before nodes containing odd values. Return the head of the modified linked list. Note: The relative order of the even nodes and the odd nodes should remain unchanged.

**Examples:**

Input: 8 -> 2 -> 4 -> 6 -> 17 -> 15 -> 9
Output: 8 -> 2 -> 4 -> 6 -> 17 -> 15 -> 9

Explanation: Since 8, 2, 4, and 6 are even, they appear first in the list, followed by the odd numbers 17, 15, and 9.

Input: 1 -> 3 -> 5 -> 7
Output: 1 -> 3 -> 5 -> 7

Explanation: There is no even number, so no modification is needed.

**Constraints:**

* The linked list contains only integers.
* The list may be empty.

**Constraints (Invented):**

* The number of nodes in the list is between 1 and 10^5 (inclusive).
* The integers in the list are within the range -10^5 to 10^5 (inclusive).
