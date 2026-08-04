# Problem: Maximum Sum Subsequence with no adjacent elements
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

class Solution:
    def solve(self, arr):
        if not arr:
            return 0
        
        include = max(arr[0], 0)
        exclude = 0
        
        for i in range(1, len(arr)):
            new_exclude = max(include, exclude)
            include = exclude + arr[i]
            exclude = new_exclude
        
        return max(include, exclude)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))