# Problem: tug-of-war
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/tug-of-war/

class Solution:
    def solve(self, arr):
        total_sum = sum(arr)
        target_sum = total_sum // 2
        
        # Create a list to store the subset sums we can achieve with elements up to i
        dp = [False] * (target_sum + 1)
        dp[0] = True  # Base case: sum of 0 is achievable with an empty set
        
        for num in arr:
            for j in range(target_sum, num - 1, -1):
                if not dp[j]:
                    dp[j] = dp[j - num]
        
        # The last index of dp that is True will be the maximum sum we can achieve with elements up to i
        current_sum = target_sum
        while not dp[current_sum]:
            current_sum -= 1
        
        subset1 = []
        subset2 = []
        for num in arr:
            if num <= current_sum and dp[num]:
                subset1.append(num)
            else:
                subset2.append(num)
        
        return [subset1, subset2]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))