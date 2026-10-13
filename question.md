# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Segregate even and odd nodes in a Linked List

**Description:** Given a Linked List of integers, The task is to modify the linked list such that all even numbers appear before all the odd numbers in the modified linked list. Also, preserve the order of even and odd numbers.

**Examples:**

1. Input: 17->15->8->12->10->5->4->1->7->6
   Output: 8->12->10->4->6->17->15->9->7
   Explanation: 8,2,4,6 are the even numbers so they appear first and 17,15,9 are odd numbers that appear later.

2. Input: 9->5->2->4->6
   Output: 2->4->6->9->5
   Explanation: There is no even number. So no need for modification.

3. Input: 8->10->12->15->17->20
   Output: 8->10->12->20->15->17
   Explanation: 8,10,12,20 are the even numbers so they appear first and 15,17 are odd numbers that appear later.

**Constraints:** 1 <= N <= 10^5 (where N is the number of nodes in the linked list)

Note: The constraints are assumed based on the context of a standard linked list problem. If specific constraints are not provided, it is assumed that the linked list can have up to 10^5 nodes.
