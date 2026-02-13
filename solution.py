# Problem: Given Sum Pair
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

class Solution:
    def solve(self, arr, target):
        num_dict = {}
        for num in arr:
            complement = target - num
            if complement in num_dict:
                return True
            num_dict[num] = True
        return False

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))