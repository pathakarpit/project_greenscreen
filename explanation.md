# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

* The Big O notation for time complexity is O(N), where N is the number of nodes in the linked list.
* The loop runs N times because it iterates over each node in the linked list once.
* The dictionary lookup `if x in dict` is not present in this code, but if we were to use a dictionary to store the values, the lookup would take O(1) time on average.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis

* The Big O notation for space complexity is O(N), where N is the number of nodes in the linked list.
* We use a dictionary/hash map to store at most N elements, which is the maximum number of nodes in the linked list.

## Step-by-Step Reconstruction Logic

* Initialize three variables:
	+ `even_dummy`: a dummy node to store the even-numbered nodes
	+ `odd_dummy`: a dummy node to store the odd-numbered nodes
	+ `even_tail`: a pointer to the last even-numbered node
	+ `odd_tail`: a pointer to the last odd-numbered node
	+ `current`: a pointer to the current node
* Initialize the `even_tail` and `odd_tail` pointers to the `even_dummy` and `odd_dummy` nodes, respectively.
* Start a loop that runs N times, where N is the number of nodes in the linked list.
* Inside the loop:
	+ Check if the current node's value is even by using the modulo operator (`current.value % 2 == 0`).
	+ If the value is even, set the `even_tail.next` pointer to the current node and move the `even_tail` pointer to the next node.
	+ If the value is odd, set the `odd_tail.next` pointer to the current node and move the `odd_tail` pointer to the next node.
	+ Move the `current` pointer to the next node.
* After the loop ends, set the `even_tail.next` pointer to the `odd_dummy.next` pointer to merge the even-numbered nodes with the odd-numbered nodes.
* Set the `odd_tail.next` pointer to `None` to terminate the odd-numbered nodes.
* Return the `even_dummy.next` pointer, which points to the merged list of even-numbered and odd-numbered nodes.
