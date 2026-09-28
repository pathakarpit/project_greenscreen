# Clone a linked list with next and random Pointer

**Difficulty:** Hard  
**Link:** [https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/](https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/)

---

## Problem Statement

**Deep Linked List Cloning Problem**

**Description:**
Given the head of a linked list that contains random pointers, clone this linked list such that each node in the new linked list has exactly the same value and points to nodes as its counterpart in the original linked list. Clone the linked list.

**Examples:**

1. **Original Linked List:** 
   1 -> (null)
   2 -> (4)
   3 -> (5)

   **Cloned Linked List:** 
   1 -> (null)
   2 -> (4)
   3 -> (5)

2. **Original Linked List:** 
   1 -> 2 -> 3
   2 -> null
   3 -> null

   **Cloned Linked List:** 
   1 -> 2 -> 3
   2 -> null
   3 -> null

3. **Original Linked List:** 
   1 -> 2 -> 3 -> 4 -> 5
   2 -> (null)
   3 -> (null)
   4 -> (null)
   5 -> (null)

   **Cloned Linked List:** 
   1 -> 2 -> 3 -> 4 -> 5
   2 -> (null)
   3 -> (null)
   4 -> (null)
   5 -> (null)


**Constraints:**

*   The linked list can have at most `10^5` nodes (`N <= 10^5`).
*   Each node's value is a non-negative integer.
*   The random pointer of each node points to any node in the linked list.
