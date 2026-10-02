# Problem: Implement Stack using Queues
# Difficulty: Easy
# Link: https://leetcode.com/problems/implement-stack-using-queues/

class Solution:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def push(self, x):
        if not self.q1:
            self.q1.append(x)
        else:
            while self.q1:
                self.q2.append(self.q1.pop(0))
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.pop(0))
    
    def pop(self):
        if not self.q1:
            raise IndexError("pop from empty stack")
        return self.q1.pop(0)
    
    def top(self):
        if not self.q1:
            raise IndexError("top of empty stack")
        return self.q1[0]
    
    def empty(self):
        return len(self.q1) == 0
    
    def size(self):
        return len(self.q1)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))