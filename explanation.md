# Professor's Analysis: Implement two stacks in an Array

## Time Complexity Analysis
### Big O Notation
The time complexity of this solution is O(N), where N is the total number of elements in the array.

### Explanation
* The loop runs N times, as we are iterating through each element in the array.
* Within the loop, the dictionary lookup `if x in dict` takes O(1) time on average, since dictionary lookups are constant-time operations in Python.
* Therefore, the overall time complexity is N * O(1) = O(N).

## Space Complexity Analysis
### Big O Notation
The space complexity of this solution is O(N), where N is the total number of elements in the array.

### Explanation
* We use a dictionary/hash map to store at most N elements, which requires O(N) extra space.

## Step-by-Step Reconstruction Logic

### Initialization
* The `arr` list is initialized with N zeros.
* The `top1` and `top2` indices are initialized to -1 and n // 2, respectively.

### Loop Condition
* The loop iterates through each element in the array from index 0 to n-1.

### Math for Finding Complement
* Within the loop, we calculate the complement as `target - current_num`.

### If/Else Logic
* If the complement is found in the dictionary, its value is returned and added to the dictionary.
* If the complement is not found in the dictionary, it is added to the dictionary with a value of 0.

### Return Statement
* If no pair is found after iterating through the entire array, -1 is returned.

Here are the steps in bullet points:

* Initialize `arr` list with N zeros and set `top1` to -1 and `top2` to n // 2.
* Iterate through each element in the array from index 0 to n-1:
	+ Calculate the complement as `target - current_num`.
	+ If the complement is found in the dictionary, return its value and add it to the dictionary.
	+ If the complement is not found in the dictionary, add it to the dictionary with a value of 0.
* If no pair is found after iterating through the entire array, return -1.
