# Delete without Head node

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/](https://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/)

---

## Problem Statement

**Title:** Delete Node in Linked List without Access to Head


**Description:**

Given a linked list where each node contains an integer data, delete a specific node from the linked list without having access to the head of the list. The deletion operation should result in the next node in the sequence taking the place of the deleted node.


**Examples:**


1. Input: Linked List: 1 -> 2 -> 3 -> 4, Node to be deleted: 2
   Output: Linked List after deletion: 1 -> 3 -> 4

2. Input: Linked List: 10 -> 20 -> 30, Node to be deleted: 20
   Output: Linked List after deletion: 10 -> 30

3. Input: Linked List: 5 -> 6 -> 7 -> 8, Node to be deleted: 7
   Output: Linked List after deletion: 5 -> 6 -> 8


**Constraints:**


- The linked list is represented as a sequence of nodes, where each node contains an integer value.
- Each node has a pointer to the next node in the sequence.
- The operation of deleting a node does not modify any other part of the linked list except for the deletion of the specified node itself.
- There are no cycles in the linked list.
- The number of nodes in the linked list is less than or equal to 10^5.
