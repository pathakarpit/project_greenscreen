# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**

**Title:** Splitting a Circular Linked List

**Description:** Given a circular linked list, split it into two halves and return the two halves as separate linked lists. The `splitList` function takes the head of the circular linked list as input and returns two linked lists, `head1` and `head2`, representing the first and second halves, respectively.

**Examples:**

1. **Input:** `head` of a circular linked list `10->4->9->10`
	* **Expected Output:** `head1` of `10->4` and `head2` of `9->10`
2. **Input:** `head` of a circular linked list `1->2->3->1`
	* **Expected Output:** `head1` of `1->2` and `head2` of `3->1`
3. **Input:** `head` of an empty circular linked list `1->1`
	* **Expected Output:** `head1` of `None` and `head2` of `None`

**Constraints:**

* The circular linked list is represented as a sequence of nodes, where each node has a `data` attribute and a `next` attribute.
* The `next` attribute of the last node points back to the first node, forming a circular linked list.
* The input linked list is assumed to be non-empty and circular.
* The `splitList` function should return two linked lists, `head1` and `head2`, representing the first and second halves of the input linked list, respectively.
* The `print_list` function is used to print the elements of a linked list, but it is not part of the solution and can be ignored.
