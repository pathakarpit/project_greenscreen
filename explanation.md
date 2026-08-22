# Professor's Analysis: Printing all solutions in N-Queen Problem

## Time Complexity Analysis
The time complexity of this solution is O(N * N).
### Explanation:

* The loop runs `N` times, where `N` is the input size.
* Inside the loop, we use a dictionary lookup `if x in dict` which takes O(1) time on average.

Therefore, N * O(1) = O(N).

## Space Complexity Analysis
The space complexity of this solution is O(N).
### Explanation:

* We use a dictionary/hash map to store at most `N` elements.

## Step-by-Step Reconstruction Logic

### Variables Initialization:
* `n`: The input size.
* `result`: A list to store the result.
* `board`: A list to store the current state of the board.

### Loop Condition:
* The loop runs `N` times, where `N` is the input size.

### Math Used:
* We use the math `target - current_num` to find the complement.

### If/Else Logic:

#### If Complement IS Found:
* We store the current state of the board in the result list.
* We move on to the next row.

#### If Complement IS NOT Found:
* We do nothing and move on to the next column.

### Return Statement:
* If no pair is found, we return an empty list.
