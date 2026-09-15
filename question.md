# Remove nth node from end of list

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/remove-nth-node-from-end-of-list/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## Problem Statement

**Title:** Remove Nth Node from End of Linked List

**Description:** Given a linked list, remove the nth node from end of list and return its head.

Note: The given list, whose nodes contain groups of integers separated by '->', not the actual list. For example:
1->2->3->4->5 
After removing the third node (with value 3), the linked list becomes :
1->2->4->5

**Examples:**
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1,2], n = 2 
Output: []

Example 3:

Input: head = [1], n = 1 
Output: []

**Constraints:** 
The number of nodes in the list is sz.
1 <= sz <= 30 (odd)
0 <= Node.val <= 100
1 <= n <= sz
