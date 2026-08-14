# Professor's Analysis: Median of Stream of Integers Running Integers

```
## Time Complexity Analysis

*   The loop runs N times where N is the number of elements in the input list.
*   Inside the loop, we perform a dictionary lookup `if x in dict` which takes O(1) time on average using hash table operations.
*   Therefore, N * O(1) = O(N).

## Space Complexity Analysis

*   The space complexity is O(N), where N is the number of elements in the input list.

## Step-by-Step Reconstruction Logic:

### 1. **Initialization**

*   An object `Solution` is created.
*   Two heaps, `self.max_heap` and `self.min_heap`, are initialized as empty lists.

### 2. **Add Number (addNum)**

*   Check if the input list (`self`) is empty or if the current number `num` is less than or equal to the negative of the root of `self.max_heap`.
    *   If true, push `-num` onto `self.max_heap`.
    *   Otherwise, push `num` onto `self.min_heap`.

### 3. **Balance Heaps**

*   Check if the length of `self.max_heap` is greater than the length of `self.min_heap` plus one.
    *   If true, pop and push the root element from `self.max_heap` to `self.min_heap`.
*   Check if the length of `self.min_heap` is greater than the length of `self.max_heap`.
    *   If true, pop and push the root element from `self.min_heap` to `self.max_heap`.

### 4. **Find Median (findMedian)**

*   Check if the lengths of `self.max_heap` and `self.min_heap` are equal.
    *   If true, calculate the median as `( (-self.max_heap[0]) + self.min_heap[0]) / 2`.
    *   Otherwise, return the negative root of `self.max_heap`.

```
