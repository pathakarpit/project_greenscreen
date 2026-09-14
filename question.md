# Multiply two numbers represented linked lists

**Difficulty:** Easy  
**Link:** [https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists/](https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists/)

---

## Problem Statement

**

**Title:** Multiplying Numbers Represented by Linked Lists using Modular Arithmetic

**Description:** 
The problem requires us to multiply two numbers represented as linked lists. To avoid overflow due to large numbers, we use modular arithmetic with modulo 10^9 + 7. We traverse both linked lists simultaneously and construct the product of the two numbers while taking into account their respective place values.

**Examples:**

1. Input:
   - First Linked List: 9 -> 4 -> 6
   - Second Linked List: 8 -> 4
   Output: 
   - Product modulo MOD = (964596 * 84) % (10^9 + 7)

2. Input:
   - First Linked List: 1 -> 2
   - Second Linked List: 3 -> 4
   Output: 
   - Product modulo MOD = (12 * 34) % (10^9 + 7)

3. Input:
   - First Linked List: 0 -> 1
   - Second Linked List: 5 -> 6
   Output: 
   - Product modulo MOD = (01 * 56) % (10^9 + 7)


**Constraints:** 

* The linked lists contain digits between 0 and 9.
* The input linked lists do not have a leading zero unless the number itself is zero.

Note: This problem assumes that the input linked lists are non-empty.
