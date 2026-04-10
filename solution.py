# Problem: Valid parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def solve(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
        
        return not stack

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))