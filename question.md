# Segregate even and odd Elements in a Linked List

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/](https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/)

---

## Problem Statement

**Title:** Divide Linked List into Even and Odd Nodes

**Description:** Given the head of a singly linked list, create a function to divide the list into two separate lists, one containing all the even numbers and the other containing all the odd numbers.

**Examples:**

1. Input: `head = [2, 1, 2, 1]`
   Output: `[2, 2]` and `[1, 1]`

2. Input: `head = [1, 3, 2, 5]`
   Output: `[2]` and `[1, 3, 5]`

3. Input: `head = [2, 2, 2, 2]`
   Output: `[2, 2, 2, 2]` and `[]`

**Constraints:**

*   The linked list contains integers.
*   The linked list has a maximum of `10^5` nodes.
*   The function should return two lists, one for even nodes and one for odd nodes.
*   If there are no even nodes, the function should return the original list.
