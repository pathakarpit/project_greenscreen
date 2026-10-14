# Professor's Analysis: Segregate even and odd Elements in a Linked List

```
## Time Complexity Analysis
### Big O Notation: O(N)

* The loop `for current_num in nums:` runs N times, where N is the number of elements in the `nums` list.
* Inside the loop, the dictionary lookup `if x in dict` takes O(1) time on average, because dictionary lookups in Python are constant time operations on average.
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis
### Big O Notation: O(N)

* We use a dictionary/hash map to store at most N elements in the `even_nums` list.

## Step-by-Step Reconstruction Logic

### Step 1: Initialize Variables
* Initialize an empty list `even_nums` to store the even numbers from the input list `nums`.

### Step 2: Loop Through Numbers
* The loop `for current_num in nums:` iterates through each number `current_num` in the input list `nums`.

### Step 3: Check for Even Numbers
* Inside the loop, we check if the current number `current_num` is even by using the modulo operator (`num % 2 == 0`).

### Step 4: Add Even Numbers to List
* If the current number is even, we add it to the `even_nums` list.

### Step 5: Return Even Numbers
* After iterating through all numbers in the input list, we return the `even_nums` list containing the even numbers.

### Step 6: No Pair Found
* If the loop completes and no pair of numbers is found, we return an empty list.
```
