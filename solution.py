# Problem: Repeat and Missing Number Array
# Difficulty: Medium
# Link: https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    def solve(self, nums):
        seen = set()
        once_set = set()
        
        for num in nums:
            if num in seen:
                once_set.discard(num)
            else:
                seen.add(num)
                once_set.add(num)
        
        if len(once_set) != 2:
            return None
        return list(once_set)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))