# Implement Stack using Queues

**Difficulty:** Easy  
**Link:** [https://leetcode.com/problems/implement-stack-using-queues/](https://leetcode.com/problems/implement-stack-using-queues/)

---

## Problem Statement

**Problem Statement:**

Implement a Stack using two Queues.
 
**Description:** 

Design an algorithm that uses two queues (`q1` and `q2`) to simulate a stack data structure. The stack should support the following operations:
- `push(x)`: adds an element `x` to the top of the stack
- `pop()`: removes the top element from the stack, or throws an error if the stack is empty
- `top()`: returns the top element of the stack without removing it
- `empty()`: checks if the stack is empty
- `size()`: returns the number of elements in the stack

**Examples:**

1. **Push**: 
   - Input: `push(1)`
   - Output: Queue `q1` contains `{}`, Queue `q2` contains `{1}`
   
2. **Pop**: 
   - Input: `pop()`
   - Output: The top element (1) is removed from the stack

3. **Top**:
   - Input: `top()`
   - Output: The current top element is 1 

4. **Size**:
   - Input: `size()`
   - Output: The number of elements in the stack is 0 

5. **Empty**:
   - Input: `empty()`
   - Output: The stack is empty

**Constraints:** 
- 1 <= x <= 10^9 (for push operation)
- The maximum number of operations performed on the stack should not exceed 10^5.

Note: Remove any solution code (C++, Python implementations) found in the text. We only want the *Question*.
