# Problem: Implement two stacks in an Array
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/

class Solution:
    def __init__(self, n):
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n // 2

    def push1(self, x):
        if self.top1 < (len(self.arr) // 2) - 1:
            self.top1 += 1
            self.arr[self.top1] = x

    def push2(self, x):
        if self.top2 < len(self.arr) - 1:
            self.top2 += 1
            self.arr[self.top2] = x

    def pop1(self):
        if self.top1 >= 0:
            ele = self.arr[self.top1]
            self.arr[self.top1] = 0
            self.top1 -= 1
            return ele
        else:
            return -1

    def pop2(self):
        if self.top2 >= len(self.arr) // 2:
            ele = self.arr[self.top2]
            self.arr[self.top2] = 0
            self.top2 -= 1
            return ele
        else:
            return -1

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))