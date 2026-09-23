# Professor's Analysis: Merge K Sorted Lists

## Time Complexity Analysis
*   **Big O:** O(N)
*   The loop runs N times because we push each element into the heap once and pop each element from the heap once.
*   The dictionary lookup `if x in dict` is not present in this code. However, the `heapq.heappush()` and `heapq.heappop()` operations take O(1) time on average, as they use a binary heap data structure internally.

## Space Complexity Analysis
*   **Big O:** O(N)
*   We use a dictionary/hash map (in this case, the Python `heap` list) to store at most N elements. Each element is stored as a tuple containing its value, index in the original list, and node reference.

## Step-by-Step Reconstruction Logic
### Initialize Variables
*   Create an empty min-heap (`heap`) and a dummy head node for the merged list (`dummy`).
*   Initialize `current` to point to the dummy head node.

### Loop Condition
*   The loop continues as long as there are elements in the heap (`while heap:`).

### Inside the Loop
*   Pop the smallest element from the heap: `(val, idx, node) = heapq.heappop(heap)`
*   Create a new node with value `val` and set its next pointer to point to the current last node of the merged list (`current.next = ListNode(val)`).
*   Move the current pointer one step forward (`current = current.next`).

### Push Next Element into Heap (if exists)
*   If there is a next node in the original list (`node.next`), push it into the heap: `heapq.heappush(heap, (node.next.val, idx, node.next))`

### Return Merged List
*   After the loop ends (i.e., when the heap is empty), return the merged list starting from `dummy.next`.
