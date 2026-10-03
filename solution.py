# Problem: Design Stack with Middle Operation
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.queue = []

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def push_to_back(self, value):
        self.queue.append(value)

    def pop_from_front(self):
        if not self.stack1 and not self.stack2 and not self.queue:
            return None
        if not self.queue:
            while self.stack1:
                self.queue.append(self.stack1.pop())
        return self.queue.pop(0)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))