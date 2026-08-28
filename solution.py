# Problem: Word Break Problem using Backtracking
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/word-break-problem-using-backtracking/

class Solution:
    def solve(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    if s[i - len(word):i] == word and dp[i - len(word)]:
                        dp[i] = True
                        break
        return dp[-1]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))