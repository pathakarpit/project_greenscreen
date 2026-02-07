# Professor's Analysis: Product of Array Except Self

## Time Complexity Analysis

* The time complexity of this solution is O(N).
* **Critical**: The loop runs N times (where N is the length of the input array `arr`), and the dictionary lookup (`if x in dict`) takes O(1) time on average. Therefore, N * O(1) = O(N).

## Space Complexity Analysis

* The space complexity is O(N).
* We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

### Initialization
* Initialize an empty list `arr` containing the input array.
* Get the length of the input array and store it in the variable `n`.

### Loop 1: Left Products
* Create an array `left_products` of size `n` with all elements initialized to 1.
* Iterate over the range (1, n) using a for loop. For each iteration:
	+ Multiply the current element at index `i-1` in `left_products` by the corresponding element at index `i-1` in the input array (`arr[i - 1]`). Store the result back in `left_products[i]`.

### Loop 2: Right Products
* Create an array `right_products` of size `n` with all elements initialized to 1.
* Iterate over the range (n-2, -1) using a for loop. For each iteration:
	+ Multiply the current element at index `i+1` in `right_products` by the corresponding element at index `i+1` in the input array (`arr[i + 1]`). Store the result back in `right_products[i]`.

### Final Calculation
* Create a new list (using list comprehension) where each element is the product of the corresponding elements from `left_products` and `right_products`.
* Return the resulting list.

### No Pair Found
* If no pair is found, return an empty list (`return []`).
