# Arithmetic Expressions

**Difficulty:** Hard  
**Link:** [https://www.hackerrank.com/challenges/arithmetic-expressions/problem](https://www.hackerrank.com/challenges/arithmetic-expressions/problem)

---

## Problem Statement

**Title**
Arithmetic Expressions | HackerRank

**Description**
We use cookies to ensure you have the best browsing experience on our website. Please read our cookie policy for more information about how we use cookies.OkProblemSubmissionsLeaderboardDiscussionsEditorial5-year-old Shinchan had just started learning mathematics. Meanwhile, one of his studious classmates, Kazama, had already written a basic calculator which supports only three operations on integers: multiplication , addition , and subtraction .  Since he had just learned about these operations, he didn't know about operator precedence, and so, in his calculator, all operators had the same precedence and were left-associative.
As always, Shinchan started to irritate him with his silly questions. He gave Kazama a list of  integers and asked him to insert one of the above operators between each pair of consecutive integers such that the result obtained after feeding the resulting expression in Kazama's calculator is divisible by . At his core, Shinchan is actually a good guy, so he only gave lists of integers for which an answer exists.
Can you help Kazama create the required expression? If multiple solutions exist, print any one of them. 

**Examples**

*   Input:
    3
    22 79 21

    Output:

    022*79-21

*   Input:
    5
    55 3 45 33 25

    Output:

    155+3-45*33-25

**Constraints**
The length of the output expression should not exceed .
You are not allowed to permute the list.
All operators have the same precedence and are left-associative, e.g.,  is interpreted as
Unary plus and minus are not supported, e.g., statements like , , or  are invalid.
