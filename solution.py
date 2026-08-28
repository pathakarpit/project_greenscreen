# Problem: Print all Palindromic Partitions of a String
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/print-palindromic-partitions-string/

class Solution:
    def solve(self, s):
        def is_palindrome(substring):
            return substring == substring[::-1]
        
        def backtrack(start, path):
            if start >= len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))