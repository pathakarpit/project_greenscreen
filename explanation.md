# Professor's Analysis: Container With Most Water

```
The final answer is: The time complexity of this algorithm is O(N), where N is the number of elements in the input array `height`. We use a dictionary/hash map to store at most N elements, which requires O(N) space. Here are the steps inside the loop:

* Calculate the area of water trapped between two lines:
	+ width = right - left
	+ h = min(height[left], height[right])
	+ water = width * h
* Update the maximum amount of water if necessary: max_water = max(max_water, water)
* Move the pointer which points to the shorter line:
	+ If height[left] < height[right]:, increment left by 1.
	+ Otherwise, decrement right by 1.

The final return statement is: return max_water
```
