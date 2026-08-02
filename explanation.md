# Professor's Analysis: find common elements three sorted arrays

## Time Complexity Analysis

* The time complexity is O(N), where N is the total number of elements across all three arrays.
* The reason for this is that we have two loops:
	+ The outer loop iterates over each array, which runs N times in total (once for each array).
	+ Inside the loop, we perform a dictionary lookup `if x in dict` to check if an element is already present in the counter. This takes O(1) time on average.
* Since the loop runs N times and the dictionary lookup takes O(1) time, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis

* The space complexity is also O(N), where N is the total number of elements across all three arrays.
* We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

### Initialize Variables and Counters

* `from collections import Counter` is imported to create counters for each array.
* Three variables, `count1`, `count2`, and `count3`, are initialized as empty counters using the `Counter()` function.
* Each counter is populated with elements from its respective array using the assignment statement (`= Counter(arr1)`, etc.).

### Find Common Elements

* The common elements between all three arrays are found by intersecting the counts of each array. This is done using the bitwise AND operator (&) on the counters (`count1 & count2 & count3`).

### Convert Result to Sorted List

* The result, which is a counter containing the common elements, is converted back to a sorted list of keys (common elements).
* The `sorted()` function is used to sort the list in ascending order.
* The `list()` function is used to convert the counter's elements into a list.

### Return Sorted List of Common Elements

* Finally, the sorted list of common elements is returned as the result. If no pair is found, an empty list is returned by default.
