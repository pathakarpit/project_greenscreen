# Problem: Count Palindromic Subsequences
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1

class Solution:
    def solve(self, s):
        n = len(s)
        if n == 0: return 0
        
        # Initialize a DP table with zeros
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome by itself
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # If the characters at both ends are the same, inherit from inner substring
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If they are different, take the maximum of excluding either end
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The result is in the top-right corner of the DP table
        return dp[0][n - 1]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))