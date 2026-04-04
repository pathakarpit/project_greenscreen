# Professor's Analysis: Mo's Algorithm

## Time Complexity Analysis
### Big O Notation
The time complexity of this solution is O(N^2).

### Explanation
* The outer loop runs N times.
* For each iteration, the inner loop also runs up to N times (worst-case scenario: all elements are part of a subarray).
* Inside the inner loop, we perform constant-time operations (addition and comparison).
* Since the inner loop runs for each element in the array, and the number of iterations is proportional to the square of the size of the input (N), the overall time complexity is O(N^2).

## Space Complexity Analysis
### Big O Notation
The space complexity of this solution is O(N).

### Explanation
* We use a list `prefix_sums` to store prefix sums, which requires O(N) space.
* We also use a variable `result` to store the indices of subarray maxima, which requires O(N) space in the worst case (when every element is part of a subarray).
* Therefore, the overall space complexity is O(N).

## Step-by-Step Reconstruction Logic
### Step 1: Initialize Variables

* Initialize an empty list `result` to store the indices of subarray maxima.
* Initialize a variable `max_prefix_sum` to negative infinity.

### Step 2: Calculate Prefix Sums

* Create a list `prefix_sums` with size `n + 1`, where `n` is the length of the input array A.
* Iterate through the array A and calculate prefix sums:
	+ Initialize `prefix_sums[0] = 0`.
	+ For each element `A[i]` in the array, calculate `prefix_sums[i + 1] = prefix_sums[i] + A[i]`.

### Step 3: Find Maximum Subarray Sum (Kadane's Algorithm)

* Iterate through the array A using two nested loops:
	+ Outer loop iterates from `i = 0` to `n - 1`.
	+ Inner loop iterates from `j = i` to `n - 1`.
* For each subarray starting at index `i`, calculate the maximum sum using Kadane's algorithm:
	+ Initialize `current_max = 0`.
	+ Iterate through the subarray, adding elements to `current_max` and updating `max_prefix_sum` if necessary.
* Store the indices of the maximum subarray maxima in the list `result`.

### Step 4: Return Result

* If no pair is found, return an empty list.
* Otherwise, return the list of indices stored in `result`.
