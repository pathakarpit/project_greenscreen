# Problem: Reverse first k elements of queue
# Difficulty: Easy
# Link: https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1

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

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))