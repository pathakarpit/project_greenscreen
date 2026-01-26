# Professor's Explanation for Maximum-Subarray

```
The final answer is: 
## Time Complexity Analysis
The time complexity of this solution is O(N), where N is the number of elements in the input list `nums`.

* The loop iterates over each element in `nums`, so it runs N times.
* Within the loop, we perform an average case dictionary lookup using `if current_sum < 0:`, which takes O(1) time on average.
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis
The space complexity of this solution is O(N), where N is the number of elements in the input list `nums`.

* We use a dictionary to store at most N elements, which takes O(N) space.

## Step-by-Step Reconstruction Logic

### Step 1: Initialize Variables

* Initialize two variables: `max_sum` and `current_sum`.
* Set `max_sum` to negative infinity (`float('-inf')`) and `current_sum` to 0.

### Step 2: Loop Through the Input List

* Iterate over each element `num` in the input list `nums`.

### Step 3: Update Current Sum

* Add the current number `num` to `current_sum`.

### Step 4: Update Maximum Sum

* If `current_sum` is greater than `max_sum`, update `max_sum` with the new value.

### Step 5: Reset Current Sum if Necessary

* If `current_sum` is less than 0, reset it to 0. This prevents accumulation of negative sums.

### Step 6: Return Maximum Sum

* After iterating over all elements in `nums`, return the maximum sum found (`max_sum`) if no pair is found that sums up to the target value.
```
