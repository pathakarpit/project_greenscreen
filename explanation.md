# Professor's Analysis: Sum of two linked lists

```
## Time Complexity Analysis
* The time complexity of this solution is O(N), where N is the total number of nodes in both linked lists.
* The loop runs N times, and each iteration performs a dictionary lookup `if x in dict` which takes O(1) time on average. Therefore, N * O(1) = O(N).
* This is because we visit each node exactly once to add the corresponding digits.

## Space Complexity Analysis
* The space complexity of this solution is O(N), where N is the total number of nodes in both linked lists.
* We use a dictionary/hash map to store at most N elements, which takes O(N) space.

## Step-by-Step Reconstruction Logic
* Initialize an empty list `result` to store the result of the addition.
* Define a nested function `add_numbers(node1, node2, carry=0)` that takes two linked lists nodes and an optional carry value as input.
	+ If both nodes are None, return a new ListNode with the carry value if it's not zero, or None otherwise. This is the base case for our recursion.
	+ Otherwise, extract the values of the current nodes `val1` and `val2`, and calculate their sum `total` along with any carry.
	+ Create a new node `result_node` with the least significant digit (LSB) of the total value (`total % 10`).
	+ Recursively call `add_numbers(node1.next, node2.next, total // 10)` to add the next digits and propagate any carry.
* Return the result of the addition by calling `add_numbers(l1, l2)`.
```
