# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Rearrange Linked List: Even Valued Nodes Before Odd Valued Nodes

**Description:** The code should rearrange the linked list so that all even-valued nodes appear before all odd-valued nodes, while maintaining their original relative order. The code should use a divide function to separate the even and odd nodes and append the remaining odd nodes to the end of the even nodes.

**Examples:**

1. Input: 1 -> 2 -> 3 -> 4 -> 5
   Output: 2 -> 4 -> 1 -> 3 -> 5

2. Input: 2 -> 4 -> 6 -> 8
   Output: 2 -> 4 -> 6 -> 8

3. Input: 1 -> 3 -> 5 -> 7
   Output: (empty list), as all nodes are odd

**Constraints:**

* The linked list is a singly linked list.
* The nodes of the linked list contain an integer value.
* The linked list is not empty.
* The values of the nodes can be any integer.
* The length of the linked list can be up to 10^6.
