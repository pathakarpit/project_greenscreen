# Professor's Analysis: Rabin-Karp Algorithm for Pattern Searching

Here's the detailed Markdown explanation allowing code reconstruction:



Time Complexity Analysis
------------------------

The time complexity of the provided Python solution is O(N).

*   The loop runs N times, where N is the number of elements in the text (T).
*   Inside the loop, we perform a dictionary lookup `if x in dict` which takes O(1) time on average.
*   Therefore, the overall time complexity is N * O(1) = O(N).



Space Complexity Analysis
-------------------------

The space complexity of the provided Python solution is O(N).

*   We use a dictionary/hash map to store at most N elements.



Step-by-Step Reconstruction Logic
---------------------------------

### Variables Initialization

*   The class Solution has two methods: `solve(self, T, P)`.
*   Inside the `solve` method:
    *   We have two constants defined: `BASE` and `MOD`, which are used for hash computation.
    *   We define a nested function `compute_hash(s, start, M)` to compute the hash value of a string from the given start index with length M.



### Computing Hash Values

*   The `compute_hash` function takes three parameters: `s` (string), `start` (index), and `M` (length).
*   It initializes an integer variable `hash_value` to 0.
*   Then, it iterates over the string from index `start` to `start + M - 1`.
*   For each character, it updates the hash value using the formula `(hash_value * BASE + ord(s[start + i]) - ord('a') + 1) % MOD`.
*   Finally, it returns the computed hash value.



### Computing Pattern and Text Hashes

*   We compute the pattern (P) hash by calling `compute_hash` with P, 0, and M.
*   We compute the text (T) hashes by applying a list comprehension to T_hashes using `compute_hash` for each index from 0 to N - M.



### Matching Pattern Hash with Text Hashes

*   We iterate over the computed text hashes (`T_hashes`) in the range of indices from 0 to len(T_hashes).
*   For each iteration, we check if the current text hash is equal to the pattern hash (P_hash) using an `if` statement.
*   If a match is found, we append the index to the result list.



### Returning Result

*   Finally, after iterating over all text hashes and checking for matches, we return the result list.
