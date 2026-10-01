# Problem: Evaluation of Postfix Expression
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/

class Solution:
    def solve(self, tokens):
        stack = []
        
        for token in tokens:
            if token not in "+-*/^":
                stack.append(int(token))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                
                if token == '+':
                    stack.append(left_operand + right_operand)
                elif token == '-':
                    stack.append(left_operand - right_operand)
                elif token == '*':
                    stack.append(left_operand * right_operand)
                elif token == '/':
                    stack.append(int(left_operand / right_operand))
                elif token == '^':
                    stack.append(left_operand ** right_operand)
        
        return stack[0]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))