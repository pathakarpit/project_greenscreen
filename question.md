# Flatten a linked list with next and child pointers

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/](https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/)

---

## Problem Statement

**Title:** Flatten Multilevel Linked List using Level Order Traversal

**Description:**

Given a linked list where in addition to the next pointer, each node has a child pointer, which may or may not point to a separate list. These child lists may have one or more children of their own to produce a multilevel linked list. Given the head of the first level of the list. The task is to flatten the list so that all the nodes appear in a single-level linked list.

**Examples:**

Input:
```
1 -> 2 -> 3
|    |
4 -> 5   6
|
7
```

Output:
```
1->4->6->2->5->7->3->8
```

Explanation:

The multilevel linked list is flattened as it has no child pointers.

**Constraints:**

* The linked list may have at most `10^5` nodes.
* Each node in the linked list has a unique integer value between 1 and `10^9`.
* The linked list may contain multiple levels of child lists.

**Approach:**

To flatten a multilevel linked list, start from the top level and process each node sequentially. For each node, if it has a child node, append this child node to the end of the current list. Continue this process for every node, updating the end of the list accordingly, until all nodes are processed and the list is flattened.

Step-by-step implementation:

1. Initialize `curr` and `tail` pointer points to head node initially.
2. Start traversing from  the first level and set the tail to the last node.
3. Start traversing from `curr` horizontally until `curr` is not `NULL`:
	* If `curr->child` is not equal to `NULL`, then append the child list to the end of the resultant list by using `tail->next = curr->child`. Traverse the child list horizontally , and set tail to the last node of the child list. Set `curr->child = NULL` to remove the link.
	* Move the `curr` pointer to the next node in the list.
4. Return the head node.

Note: The solution code has been removed from the raw text, leaving only the problem statement and explanation.
