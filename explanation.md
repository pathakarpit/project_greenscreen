# Professor's Analysis: Longest Substring without Repeating Characters

The final answer is: 

## Time Complexity Analysis
### O(N) Time Complexity

* The loop runs N times, where N is the number of students.
* Inside the loop, we perform a dictionary lookup `if x in dict` which takes O(1) time on average.
* Since the loop runs N times and each iteration involves a constant-time operation (dictionary lookup), the overall time complexity is N * O(1) = O(N).

## Space Complexity Analysis
### O(N)

* We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

* Initialize `total_height` as 0 and `num_students` as the length of the input list `heights`.
* Calculate the average height by dividing `total_height` by `num_students`: `average_height = total_height / num_students`.
* Iterate over each element in the input list `heights`.
	+ For each student, subtract their height from the average height to find their complement: `(target - current_num)`.
	+ If the complement is found (not shown in the provided code), return the average height rounded to 2 decimal places using `round(average_height, 2)`.
* If no pair of students with equal total height is found after processing all students, return an empty result (not shown in the provided code).
