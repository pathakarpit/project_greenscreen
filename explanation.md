# Professor's Analysis: Maximum Possible Number by doing at most K swaps

**
The final answer is:

## Time Complexity Analysis

### Big O Notation:
The time complexity of this solution is O(N).

### Explanation:
*   The loop runs N times and the dictionary lookup takes O(1) time on average.
*   Therefore, N \* O(1) = O(N).

## Space Complexity Analysis

### Big O Notation:
The space complexity of this solution is O(N).

### Explanation:
*   We use a dictionary to store at most N elements.

## Step-by-Step Reconstruction Logic

### Initialize Variables
Create an empty dictionary called `index_map`.

### Loop 1: Populate Index Map
*   Iterate through each element `num` at index `i` in the input array `nums`.
    *   Store the index `i` of the current number `num` in the `index_map` with `num` as the key.

### Loop 2: Rearrange Array
*   Iterate through each element `num` in the input array `nums`.
    *   Check if the complement `(k - num)` is present in the `index_map` and we haven't exceeded the length of the input array (`len(rearranged) < len(nums)`).
        +   If both conditions are true, append `num` to the `rearranged` list.

### Return Statement
After the loops, return the rearranged list `rearranged`.
