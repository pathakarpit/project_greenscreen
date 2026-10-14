# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

* **Big O:** O(N)
* **Explanation:** The loop runs N times, where N is the number of nodes in the linked list. Inside the loop, we are performing a dictionary lookup `if x in dict` which takes O(1) time on average. Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis

* **Big O:** O(N)
* **Explanation:** We use a dictionary/hash map to store at most N elements, where N is the number of nodes in the linked list.

## Step-by-Step Reconstruction Logic

* **Initialization:**
	+ `even_head` and `even_tail` are initialized as `None`.
	+ `odd_head` and `odd_tail` are initialized as `None`.
	+ `current` is initialized as the head of the linked list.
* **Loop Condition:** The loop continues as long as `current` is not `None`.
* **Math inside Loop:** Inside the loop, we calculate `current.data % 2` to determine if the current node's data is even or odd.
* **Logic inside Loop:**
	+ If the current node's data is even:
		- If `even_head` is `None`, set `even_head` to the current node and `even_tail` to the current node.
		- Otherwise, set `even_tail.next` to the current node and `even_tail` to the current node.
	+ If the current node's data is odd:
		- If `odd_head` is `None`, set `odd_head` to the current node and `odd_tail` to the current node.
		- Otherwise, set `odd_tail.next` to the current node and `odd_tail` to the current node.
	+ Move `current` to the next node in the linked list.
* **After Loop:**
	+ If `even_tail` is not `None`, set `even_tail.next` to `odd_head`.
	+ If `odd_tail` is not `None`, set `odd_tail.next` to `None`.
* **Return Statement:**
	+ If `even_head` is not `None`, return `even_head`.
	+ Otherwise, return `odd_head`.

This logic is used to separate the linked list into two new linked lists: one for even numbers and one for odd numbers. The two linked lists are then concatenated, with the even numbers linked list coming first. If the original linked list contained only odd numbers, the function returns the odd numbers linked list.
