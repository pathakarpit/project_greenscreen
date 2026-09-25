# Professor's Analysis: Quicksort on singly-linked list

## Time Complexity Analysis

* The Big O is O(N).
* The loop runs N times, where N is the number of elements in the linked list.
* Inside the loop, we perform a dictionary lookup `if x in dict`, which takes O(1) time on average. Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis

* The Big O is O(N).
* We use a dictionary/hash map to store at most N elements from the linked list.

## Step-by-Step Reconstruction Logic

* Initialize variables: `head` (the input linked list), `node_list` (an empty list to store nodes from the linked list), and `current` (a pointer to traverse the linked list).
* Check if the input linked list is empty or only contains one node. If so, return the input linked list.
* Define a helper function `quick_sort(start, end)` to partition and sort the linked list using Quick Sort:
	+ If the sub-list contains only one node or two nodes, return without sorting.
	+ Select a pivot node from the start of the sub-list.
	+ Reorder the sub-list such that all elements less than the pivot are on its left and all elements greater are on its right.
	+ Swap the pivot with the node at the end of the sorted left sublist (left).
	+ Recursively call `quick_sort` on the left and right partitions of the sub-list.
* Convert the linked list to a list for sorting:
	+ Initialize an empty list `node_list`.
	+ Traverse the linked list using the `current` pointer, appending each node to `node_list`.
* Call the `quick_sort` function on the entire linked list (using `node_list[0] as the start and None as the end).
* Rebuild the sorted linked list from the sorted list:
	+ Iterate over the sorted list and set the `next` pointer of each node to the next node in the sorted order.
	+ Set the `next` pointer of the last node to `None`.
* Return the head of the sorted linked list. If no pair is found, return the original input linked list.

This step-by-step reconstruction should allow a developer to rewrite the code based on this explanation alone.
