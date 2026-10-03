# Professor's Analysis: Reverse first k elements of queue

```
class Solution:
    def solve(self, k, queue):
        if k == 0 or not queue:
            return queue
        
        stack = []
        for _ in range(k):
            stack.append(queue.pop(0))
        
        while stack:
            queue.append(stack.pop())
        
        return queue
```
