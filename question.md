# Best time to Buy and Sell Stock

**Difficulty:** Medium  
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## Problem Statement

**Problem Statement:**
Maximize Two Transaction Profit

Given an array of stock prices `prices` where `n >= 2`, find the maximum total profit that can be achieved by buying and selling stocks, considering two transactions.

**Description:**

Analyze the given JavaScript solution for maximizing profit through two transactions. The algorithm uses dynamic programming to optimize space complexity while achieving a time complexity of O(n). However, the core problem statement focuses on finding the maximum total profit with two transactions allowed.

**Examples:**

1. **Example 1:** `prices = [2, 3, 5]`

   *   Initial investment at price 2
   *   Sell at 3 (Transaction 1)
   *   Buy at 4 (new low after sell) and sell at 5 (Transaction 2)

   Expected Output: Max profit with two transactions = 7

2. **Example 2:** `prices = [6, 5, 4, 3, 2]`

   *   No profitable transaction can be made in this case.

   Expected Output: Max profit with two transactions = 0

3. **Example 3:** `prices = [7, 1, 5, 3, 6, 4]`

   *   Sell at 7 (Transaction 1)
   *   Buy at 2 and sell at 5 (Transaction 2)

   Expected Output: Max profit with two transactions = 9

**Constraints:** 

*   `n >= 2`, where `n` is the length of the array
*   No upper bound on prices, but it's assumed that there will be no extremely high values affecting performance.
*   The algorithm should achieve a time complexity of O(n) and space complexity of O(1), implying that it must use efficient dynamic programming techniques to optimize memory usage.
