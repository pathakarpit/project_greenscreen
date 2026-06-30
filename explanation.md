# Professor's Analysis: Boyer Moore Algorithm for Pattern Searching

## Time Complexity Analysis

* The time complexity is O(N), where N is the length of the input string `txt`.
* The loop runs N times, and for each iteration, we perform a constant-time dictionary lookup `if x in dict` which takes O(1) time on average.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis

* The space complexity is O(N), where N is the length of the input string `txt`.
* We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

###  Initialization
* Initialize an empty dictionary `last_occurrence` to store the last occurrence of each character in the input string.
* Initialize two variables: `n` to store the length of the input string and `m` to store the length of the pattern.

### Loop Iteration
* The loop runs from `i = m - 1` to `n`, where `n` is the length of the input string.
* In each iteration, we perform the following steps:
	+ Initialize two pointers: `j` and `k`. `j` points to the last character of the pattern, and `k` points to the current position in the input string.
	+ Compare the characters at positions `j` and `k`. If they match, decrement both pointers (`j -= 1` and `k -= 1`) and repeat this step until we reach the start of the pattern or a mismatch is found.
	+ If no mismatch is found (i.e., `j < 0`), it means that the pattern has been completely matched. In this case:
		- Append the current position (`k + 1`) to the list of matches.
		- Calculate the shift value using the bad character heuristic: `shift = max(1, k - last_occurrence.get(txt[k], -2))`.
	+ If a mismatch is found (i.e., `j >= 0`), it means that we need to shift the pattern. In this case:
		- Calculate the shift value using the bad character heuristic: `shift = max(1, j - last_occurrence.get(txt[k], -2))`.
	+ Increment the loop counter (`i += shift`) and repeat the iteration.

### Final Return
* If no pair is found after iterating through the entire input string, return an empty list.
* Otherwise, return the list of matches.
