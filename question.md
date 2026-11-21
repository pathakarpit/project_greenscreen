# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

Title: Rearrange Linked List by Even and Odd Nodes

Description: Given the head of a singly linked list , rearrange the list in place so that all nodes containing even values appear before nodes containing odd values. Return the head of the modified linked list .

Examples:
 
Input:  Output: 8 -> 2 -> 4 -> 6 -> 17 -> 15 -> 9
Explanation: Since 8, 2, 4, and 6 are even, they appear first in the list, followed by the odd numbers 17, 15, and 9.

Input:  Output: 1 -> 3 -> 5 -> 7
Explanation: There is no even number, so no modification is needed.

Input:  Output: 2 -> 4 -> 6 -> 8 -> 10
Explanation: Only even numbers are present in the list.

Constraints:
 
- The relative order of the even nodes and the odd nodes should remain unchanged.
- Note: The linked list does not have a tail.

Problem Constraints:

1 <= N <= 10^5

Algorithm:
 
1. Create two separate linked lists, one for even nodes and one for odd nodes.
2. Traverse the original linked list and add each even-valued node to the even list and each odd-valued node to the odd list, preserving their original order.
3. After traversal, the even list becomes 0 -> 4 -> 6 -> 10 and the odd list becomes 1 -> 9 -> 11.
4. If there are no even nodes, return the original list.
5. Append the remaining odd nodes after the even nodes and return the result list (starting with even nodes).

Time Complexity:
 
O(n) where n is the number of nodes in the linked list.

Space Complexity:
 
O(1) as we are not using any extra space.
