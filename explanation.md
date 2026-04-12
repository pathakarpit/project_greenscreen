# Professor's Analysis: Remove Consecutive Characters

## Time Complexity Analysis


The time complexity of this solution is O(N).


• The loop runs N times, where N is the number of characters in the string `s`.
• Inside the loop, we perform an average-case dictionary lookup using `if char in result`, which takes O(1) time.
• Therefore, the total time complexity is N * O(1) = O(N).


## Space Complexity Analysis


The space complexity of this solution is O(N).


• We use a list (`result`) to store at most N characters.


## Step-by-Step Reconstruction Logic


To reconstruct the logic behind this code, follow these steps:


### Initialize Variables

* `result`: an empty list to store the compressed string
* `char`: each character in the input string `s`

### Loop Through Characters in String

* Iterate through each character `char` in the input string `s`
* Use a condition to check if the current character is different from the last character in the result list (`result[-1] != char`)

### Append Character to Result List

* If the current character is not equal to the last character, append it to the result list
* Continue with the next iteration of the loop

### Return Compressed String

* After iterating through all characters in the string, return the compressed string by joining all characters in the result list (`''.join(result)`)


Note that if no pair is found, an empty string will be returned.
