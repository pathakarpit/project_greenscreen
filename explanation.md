# Professor's Analysis: majority element

```
## Time Complexity Analysis
* The loop `for num in arr:` runs N times, where N is the number of elements in the input array `arr`.
* Inside the loop, we perform a dictionary lookup `if x in dict` which takes O(1) time on average using Python's built-in `dict` data structure.
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis
* We use a dictionary to store at most N elements.
* The space complexity is therefore O(N), where N is the number of unique elements in the input array.

## Step-by-Step Reconstruction Logic

### Initialize Variables

* `candidate` is initialized as `None`.
* `count` is initialized as `0`.

### Loop Through Array

* We iterate through each element `num` in the input array `arr`.
* If `count` is `0`, we set `candidate` to `num` and increment `count` to `1`.
* If `candidate` is equal to `num`, we increment `count` by `1`.
* If `candidate` is not equal to `num`, we decrement `count` by `1`.

### Verify Majority Element

* We iterate through the input array again and count the occurrences of the candidate element.
* If the count of the candidate element is greater than half the length of the array, we return the candidate element.

### Return Result

* If no pair with sum equal to target is found after iterating through all elements, we return `-1`.
```
