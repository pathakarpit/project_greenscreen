# Problem: Permute Two Arrays such that Sum of Every Pair is Greater or Equal to K
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/permute-two-arrays-sum-every-pair-greater-equal-k/

class Solution:
    def solve(self, a, b, k):
        for i in range(len(a)):
            if a[i] + b[i] < k:
                return False
        return True

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))