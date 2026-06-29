# Professor's Analysis: Word Wrap

```markdown
## Time Complexity Analysis
### Big O Notation
The time complexity of this solution is O(N), where N is the number of lines in the raw text.

### Explanation
The loop runs `N` times, and each iteration involves checking if the current line contains specific keywords ("Input:", "Output:", "Examples", "Constraints") and performing dictionary lookups (`if x in dict`). The dictionary lookup `if x in dict` takes O(1) time on average. Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis
### Big O Notation
The space complexity of this solution is O(N), where N is the number of lines in the raw text.

### Explanation
We use a dictionary/hash map to store at most `N` elements, which represents the extracted information from the raw text (problem statement, description, examples, and constraints).

## Step-by-Step Reconstruction Logic

* Initialize variables:
	+ `raw_text`: the input string containing the problem statement and other relevant information
	+ `lines`: a list of strings representing each line in the raw text
	+ `problem_statement`, `description`, `examples`, `constraints`: empty lists to store extracted information
* Iterate over each line in `lines`:
	+ Check if the current line contains "Input:" and `len(examples) == 0`; if true, skip this iteration (`continue`)
	+ Check if the current line contains "Output:"; if true, break out of the loop
	+ Check if the current line contains "Examples"; if true, extract the example description by replacing "Examples:" with an empty string and strip leading/trailing whitespace; append it to `examples`
	+ Check if the current line contains "Constraints"; if true, split the constraint lines by "," and iterate over each constraint:
		- Strip leading/trailing whitespace from the constraint
		- Append it to `constraints`
	+ If none of the above conditions are met, check if this is the first iteration (i.e., `problem_statement` and `description` are empty); if true, append the current line to `problem_statement`
	+ Check if the current line contains "Description:"; if true, append the description text (excluding the prefix) to `description`
* After iterating over all lines, construct a dictionary containing extracted information (`extracted_info`) with keys "problem_statement", "description", "examples", and "constraints"
* Return the constructed dictionary (`extracted_info`)
```
