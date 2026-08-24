# Problem: Partition Equal Subset Sum
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1

class Solution:
    def solve(self, arr, target):
        seen = set()
        for num in arr:
            complement = target - num
            if complement in seen:
                return True
            seen.add(num)
        return False

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))