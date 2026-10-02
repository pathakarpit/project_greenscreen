# Problem: Implement Stack Queue using Deque
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/implement-stack-queue-using-deque/

class Solution:
    def __init__(self):
        self.stack = deque()
        self.queue = deque()
    
    def solve(self, operation, value=None):
        if operation == "push":
            self.stack.appendleft(value)  # Push to the top of the stack
            self.queue.append(value)       # Enqueue at the rear of the queue
        elif operation == "pop":
            if self.stack:
                self.stack.popleft()      # Pop from the top of the stack
            if self.queue:
                self.queue.popleft()     # Dequeue from the front of the queue
        elif operation == "peek_stack":
            return self.stack[0]          # Peek at the top element of the stack
        elif operation == "peek_queue":
            return self.queue[0]          # Peek at the front element of the queue
        elif operation == "is_empty_stack":
            return not bool(self.stack)   # Check if the stack is empty
        elif operation == "is_empty_queue":
            return not bool(self.queue)   # Check if the queue is empty
        
# Example usage:
# s = Solution()
# s.push(3)  # Push element 3 onto the stack and enqueue it in the queue
# s.pop()    # Pop an element from the stack and dequeue an element from the queue

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))