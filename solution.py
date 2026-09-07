# Problem: Arithmetic Expressions
# Difficulty: Hard
# Link: https://www.hackerrank.com/challenges/arithmetic-expressions/problem

class Solution:
    def solve(self, nums):
        from itertools import product
        
        # Define the operations
        ops = ['*', '+', '-']
        
        # Generate all possible combinations of operators between numbers
        for op_combo in product(ops, repeat=len(nums) - 1):
            expression = ''
            for i in range(len(nums)):
                if i > 0:
                    expression += op_combo[i-1]
                expression += str(nums[i])
            
            # Evaluate the generated expression and check divisibility
            try:
                result = eval(expression)
                if result % (len(nums) - 1) == 0:
                    return expression
            except Exception as e:
                continue
        
        return None

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))