# Design Stack with Middle Operation

**Difficulty:** Medium  
**Link:** [https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/](https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/)

---

## Problem Statement

**Title:** Implementing Two Stacks as One with Efficient Push and Pop Operations


**Description:** Design an algorithm that uses two stacks and a queue to efficiently handle push_to_back() and pop_from_front() operations while maintaining the order of elements.


**Examples:**

1. **Example 1:**
   - Input: `stack.push(1); stack.push(2)`
   - Output: `stack.pop()` returns `2`
   - Explanation: The two stacks will be `[1, 2]` and an empty queue.
   - Expected output is `2`, which is the top element of the combined stack.

2. **Example 2:**
   - Input: `stack.push(1); stack.push(2); stack.push_to_back(3)`
   - Output: `stack.pop_from_front()` returns `3`
   - Explanation: The two stacks will be `[1, 2]` and the queue will have been filled in reverse order as `[3]`, then the first element of each is popped to get `[2, 1, 3]`. 
   - Expected output is `3`, which is the front element of the combined stack.

3. **Example 3:**
   - Input: `stack.push(1); stack.push(2)`
   - Output: `stack.pop_from_front()` returns `None`
   - Explanation: There are no elements in the queue, and both stacks are empty.
   - Expected output is `None`, indicating that there are no more elements to pop.


**Constraints:** 

- 1 <= N <= 10^5 (assuming N is the number of operations performed)
- Each push operation takes an integer value between 1 and 10^9
- Each pop operation returns an integer value between 1 and 10^9
