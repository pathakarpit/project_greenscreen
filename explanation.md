# Professor's Analysis: Allocate Minimum number of Pages

## Time Complexity Analysis
### Big O Notation:
The time complexity of this solution is O(N).

### Explanation:

* The loop runs N times, where N is the length of the input list `arr`.
* Inside the loop, we perform a dictionary lookup to see if an element is present in the dictionary. This takes O(1) time on average.
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis
### Big O Notation:
The space complexity of this solution is O(N), where N is the maximum number of elements stored in the dictionary.

### Explanation:

* We use a dictionary to store at most N elements. Each element takes constant space, so the total space used by the dictionary is proportional to N.

## Step-by-Step Reconstruction Logic
### Loop Initialization:
* Initialize two pointers `left` and `right`, representing the minimum and maximum possible values of the `mid` variable.
* The minimum value `left` is set to the maximum element in the input list `arr`.
* The maximum value `right` is set to the sum of all elements in the input list `arr`.

### Loop Condition:
* The loop continues until `left <= right`.

### Loop Body:
* Inside the loop, we calculate the middle value `mid` using the formula `(left + right) // 2`.
* We then call the function `is_possible(mid)` to check if it is possible to distribute the books among the students with `k` bins.
* If `is_possible(mid)` returns `True`, it means that we have found a valid distribution of books, and we update the result variable `result` to store the minimum number of pages per student.

### Function `is_possible(mid)`:
* Initialize two variables: `students` (number of students) and `current_sum` (current sum of pages).
* Iterate over each page in the input list `arr`.
	+ If a page is greater than `mid`, return `False` because it is not possible to distribute this book among the students with `k` bins.
	+ If adding the current page to the `current_sum` does not exceed `mid`, add the page to the `current_sum`.
	+ Otherwise, increment the number of students by 1 and update the `current_sum` to store the current page (since all previous pages will be reassigned to this new student).
* If we have more than `k` students after iterating over all pages, return `False` because it is not possible to distribute the books among the students with `k` bins.
* Finally, return `True` if no problems were encountered.

### Return Statement:
* After exiting the loop, return the value of the result variable `result`, which stores the minimum number of pages per student. If no valid distribution was found, return `-1`.
