# Professor's Analysis: Group Anagrams

## Time Complexity Analysis

* The time complexity of this solution is O(N).
* This is because the loop runs N times, where N is the number of words in the input list.
* Inside the loop, there is a dictionary lookup `if x in dict` to check if a sorted word is already in the `anagrams` dictionary. On average, dictionary lookups take constant time O(1).
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis

* The space complexity of this solution is O(N).
* This is because we use a dictionary to store at most N elements, where N is the number of words in the input list.

## Step-by-Step Reconstruction Logic

### Step 1: Initialize variables

* Create an empty dictionary `anagrams` to store anagrams.
* Initialize an empty list `words` to store the input words.

### Step 2: Loop through each word

* For each word `word` in the input list `words`, perform the following steps:
	+ **Step 3:** Sort the characters of the word and join them into a string `sorted_word`.

### Step 3: Create or retrieve anagram group

* If `sorted_word` is not already in the `anagrams` dictionary, create a new empty list for it.
* Otherwise, retrieve the existing list of anagrams for `sorted_word`.

### Step 4: Add word to anagram group

* Append the original unsorted word `word` to the list of anagrams for `sorted_word`.

### Step 5: Return anagram groups

* After processing all words, return a list of lists containing the anagram groups.
	+ Each inner list represents a set of anagrams that are permutations of each other.

Here's the final code based on these steps:
```python
class Solution:
    def solve(self, words):
        anagrams = {}
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        
        return list(anagrams.values())
```
