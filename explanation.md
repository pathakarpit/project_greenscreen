# Professor's Analysis: Wildcard String Matching

## Time Complexity Analysis

* The Big O notation for this problem is O(N).
* CRITICAL: The loop runs N times, where N is the length of the text. Within the loop, we perform a dictionary lookup `if x in dict` which takes O(1) time on average.
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis

* The Big O notation for this problem is O(N).
* We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

### Initialization
* Initialize an empty dictionary `memo` to store the results of subproblems.
* Define a nested function `is_match(i, j)` that will be used to check if the pattern matches the text at indices `i` and `j`.

### Loop Condition
* The loop condition for the outer loop is `i < len(text)`, which ensures that we process each character in the text exactly once.

### Complement Calculation
* Within the loop, calculate the complement of the current number as `target - current_num`.
* This value will be used to look up the dictionary and retrieve the stored result if available.

### Dictionary Lookup
* Perform a dictionary lookup `if x in dict` using the calculated complement as the key.
* If the key is found in the dictionary, return the stored result immediately.

### Recursive Call
* If the key is not found in the dictionary, make a recursive call to `is_match(i + 1, j)` if the current character matches the pattern or if the pattern is '?' (wildcard).
* Alternatively, make another recursive call to `is_match(i, j + 1)` if the pattern has more characters and the current character does not match.

### Handling '*' Pattern
* If the pattern is '*', then we have two possibilities:
	+ Either the current character matches the previous one (`first_match` is True), in which case we make a recursive call to `is_match(i + 1, j)`.
	+ Or the current character does not match, but we can still try to find a match by making a recursive call to `is_match(i, j + 1)`.

### Return Statement
* If no pair is found after processing all characters in the text, return False to indicate that there is no solution.
* Otherwise, return True to indicate that a valid pair has been found.
