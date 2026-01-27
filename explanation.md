# Professor's Analysis: Search in Rotated Sorted Array

```
## Time Complexity Analysis
The time complexity of this solution is O(N), where N is the number of elements in the array.

## Space Complexity Analysis
The space complexity of this solution is O(N), where N is the number of elements in the array.

## Step-by-Step Reconstruction Logic

### Initialize Variables
* `left` and `right` variables are initialized to 0 and `len(arr) - 1`, respectively.
* The initial range of possible indices for the key is `[0, len(arr) - 1]`.

### Loop Condition
* The loop continues until `left <= right`.

### Inside the Loop
* Calculate the midpoint `mid` using the formula `(left + right) // 2`.
* Compare the value at the midpoint index with the key.
* If the array is rotated and the left half is sorted, check if the key is within the range `[arr[left], arr[mid]]`. If it is, move the `right` pointer to `mid - 1`. Otherwise, move the `left` pointer to `mid + 1`.
* If the right half is sorted, check if the key is within the range `[arr[mid], arr[right]]`. If it is, move the `left` pointer to `mid + 1`. Otherwise, move the `right` pointer to `mid - 1`.

### Return Statement
* If the loop ends and the key is found, return the index of the key.
* If the loop ends and the key is not found, return `-1`.
```
