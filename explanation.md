# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

* Big O: O(N)
* The loop runs N times, where N is the number of nodes in the linked list.
* Within the loop, we have a dictionary lookup `if x in dict` which takes O(1) time on average.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis

* Big O: O(1)
* We use a dictionary/hash map to store at most N elements, but the size of the dictionary is constant because we are only storing the head of the even and odd lists.

## Step-by-Step Reconstruction Logic

* Initialize variables:
	+ `even_head`: set to `head.next`
	+ `even`: set to `even_head`
	+ `odd`: set to `head`
* The loop condition is `while even and even.next`:
	+ In each iteration, we do the following:
		- `odd.next = even.next`: update the next pointer of the current odd node to point to the next even node
		- `odd = odd.next`: move to the next odd node
		- `even.next = odd.next`: update the next pointer of the current even node to point to the next odd node
		- `even = even.next`: move to the next even node
* After the loop, we update `odd.next = even_head` to link the odd list to the even list.
* Finally, we return `head` to get the modified linked list.
