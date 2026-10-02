# Implement Stack Queue using Deque

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/implement-stack-queue-using-deque/](https://www.geeksforgeeks.org/implement-stack-queue-using-deque/)

---

## Problem Statement

**Title:** Implement Stack and Queue using Deque

**Description:** 
Implement a stack and queue data structure using a deque in Java, where elements are added and removed from the top of the stack and rear of the queue respectively.

**Examples:**

1. **Stack Example**
   - Input: Create a stack with elements [3, 2, 1]
   - Output: Stack: [3, 2, 1]
   - Operation: Pop an element from the stack
   - Output: Stack after pop: [2, 1]

2. **Queue Example**
   - Input: Create a queue with elements [1, 2, 3]
   - Output: Queue: [1, 2, 3]
   - Operation: Dequeue an element from the queue
   - Output: Queue after dequeue: [2, 3]

3. **Mixed Example**
   - Input: Create a stack with elements [4, 5, 6] and a queue with elements [7, 8, 9]
   - Output: Stack: [6, 5, 4], Queue: [7, 8, 9]
   - Operation: Push an element onto the stack and enqueue an element onto the queue
   - Output: Stack after push: [6, 5, 4, 10], Queue after enqueue: [7, 8, 9, 11]

**Constraints:** 
*   The input size for both the stack and queue can be up to 10^5 elements.
*   The deque implementation should support push (add to top) and pop operations for the stack, as well as add (enqueue) and remove (dequeue) operations for the queue.
