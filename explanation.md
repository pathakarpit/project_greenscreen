# Professor's Analysis: Write a Function to get the Intersection Point of two Linked Lists

```
## Time Complexity Analysis

* The loop `for _ in range(abs(lenA - lenB)):` runs N times, where N is the length of the longer linked list.
* Inside this loop, we either move `headA` or `headB` to match the starting point of the shorter list. This takes O(1) time on average because dictionary lookups are constant time in Python.
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis

* The space complexity is O(1), as we only use a few extra variables to store the lengths of the linked lists and the pointers `headA` and `headB`. We do not use any data structures that grow with the input size.

## Step-by-Step Reconstruction Logic

### Step 1: Initialize Variables
* Define two helper functions: `get_length(head)` returns the length of a linked list, and `solve(headA, headB)` is the main function to find the intersection point.
* Initialize `lenA` and `lenB` to store the lengths of the linked lists.

### Step 2: Find Lengths of Linked Lists
* Use the `get_length(head)` helper function to find the length of both linked lists (`headA` and `headB`) and store them in `lenA` and `lenB`.

### Step 3: Move Longer List's Pointer
* Compare the lengths of the two linked lists using `abs(lenA - lenB)`.
* Use a loop to move the pointer of the longer list to match the starting point of the shorter list. This is done by incrementing `headA` or `headB` accordingly.

### Step 4: Find Intersection Point
* Once both pointers are at the same distance from the end of their lists, compare them using a while loop.
* If the current nodes are equal (`headA == headB`), return either `headA` or `headB`, as they point to the same node.

### Step 5: Return None if No Intersection Found
* If the while loop completes without finding an intersection, return `None`.
```
