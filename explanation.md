# Professor's Analysis: Delete nodes which have a greater value on right side

## Time Complexity Analysis
The Big O notation for this algorithm is O(N).

* The loop runs N times because we are traversing through a linked list of size N.
* Inside the loop, the dictionary lookup `if current.next.val > current.next.next.val` takes O(1) time on average in Python due to its hash table implementation. 
* Therefore, the overall time complexity is N * O(1) = O(N).

## Space Complexity Analysis
The Big O notation for space complexity is O(N).

* We use a dictionary/hash map (in this case, we don't actually use one explicitly but let's assume that was an oversight) to store at most N elements. However, the real space usage comes from the linked list itself which in this algorithm is O(N) as it stores all the nodes.

## Step-by-Step Reconstruction Logic

* Initialize a dummy node `dummy` with value 0 and point its next pointer to the head of the linked list.
* Set `current` pointer to the dummy node.
* The loop condition checks for two consecutive nodes (`current.next` and `current.next.next`) before it increments `current`.
* Inside the loop:
	+ If the value of the next node is greater than the one after that, we remove the next node by changing the current node's next pointer to point directly at the node after the removed node (essentially "skipping" the current node's next node).
	+ Otherwise, increment `current` to move to the next pair of nodes.
* This process repeats until it has iterated over the entire list or found all pairs that need swapping.
* The function returns `dummy.next`, effectively skipping the dummy node and returning the head of the modified linked list.

If you follow these steps carefully, you should be able to implement this algorithm from scratch. Remember that at each iteration we are essentially comparing two adjacent nodes in the linked list (and their values) to determine whether they need swapping, which reduces the overall number of nodes in the list if there were any "reverse" pairs initially.
