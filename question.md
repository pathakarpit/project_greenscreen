# Implement two stacks in an Array

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/](https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/)

---

## Problem Statement

**Title:** Implementing Two-Stack Data Structure

**Description:** Design and implement a two-stack data structure that utilizes an array of size `n` to store elements. The stack at index `0` to `mid - 1` is denoted as `stack1`, while the stack at index `mid` to `n - 1` is denoted as `stack2`. Implement the following operations: `push1(x)`, `push2(x)`, `pop1()`, and `pop2()`.

**Examples:**

1. Initial Setup:

   * `arr`: `[0, 0, ..., 0]`
   * `top1`: `-1`
   * `top2`: `-1`

   Input: `n = 10` (size of the array)

   Output: None

2. Pushing Elements to Stack1 and Stack2:

   Input: `push1(5)`, `push2(3)`, `push1(8)`, `push2(6)`

   Output: 

   * `arr`: `[0, 5, 0, 0, 3, 0, 0, 0, 0, 0]` (after pushing 5 to stack1)
   * `top1`: `0`
   * `top2`: `-1`

   * `arr`: `[0, 5, 0, 0, 3, 8, 0, 0, 0, 0]` (after pushing 8 to stack1)

   * `arr`: `[0, 5, 0, 0, 3, 8, 0, 6, 0, 0]` (after pushing 6 to stack2)

3. Popping Elements from Stack1 and Stack2:

   Input: `pop1()`, `pop2()`

   Output: 

   * `arr`: `[0, 5, 0, 0, 3, 8, 0, 6, 0, 0]` (initial state)

   * `ele = 5` (popped from stack1)
   * `top1`: `-1`
   * `top2`: `-1`

4. Popping Elements from Empty Stacks:

   Input: `pop1()`, `pop2()`

   Output: 

   * `ele = -1` (popped from empty stack1)
   * `arr`: `[0, 0, ..., 0]`
   * `top1`: `-1`
   * `top2`: `-1`

**Constraints:** 

* The size of the array (`n`) should be a positive integer.
* The value of `mid` is calculated as `n / 2`.
* The top indices (`top1` and `top2`) are initially set to `-1`, indicating that both stacks are empty.

Note: This problem assumes that the implementation uses an array of size `n` to store elements, with `stack1` at index `0` to `mid - 1` and `stack2` at index `mid` to `n - 1`.
