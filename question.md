# Linked list in zig-zag fashion

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/](https://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/)

---

## Problem Statement

```
Title: Zig-Zag Linked List Rearrangement
Description: Given the head of a linked list, rearrange the nodes to form a zig-zag pattern: a ≤ b ≥ c ≤ d ≥ e ≤ f ... It means the first pair (a, b) is increasing, second pair (b, c) is decreasing, third pair (c, d) is increasing and so on in the modified linked list. Only swapping of adjacent nodes is allowed.
Examples:
1. Input: 
   1 -> 2 -> 3 -> 4 -> 5
   Output: 
   1 -> 3 -> 2 -> 4 -> 5

2. Input: 
   A -> B -> C -> D -> E
   Output: 
   A -> C -> B -> E -> D

3. Input: 
   X -> Y -> Z -> W -> V
   Output: 
   X -> Z -> Y -> V -> W

Constraints:
* The linked list can have any number of nodes.
* The nodes are uniquely identifiable by their values (integers).
* No adjacent nodes should be the same.
```
