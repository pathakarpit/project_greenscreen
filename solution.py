# Problem: Find Pair with Sum in Sorted & Rotated Array
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/?ref=lbp

class Solution:
    def solve(self, arr, target):
        n = len(arr)
        left, right = 0, n - 1
        
        # Find the pivot point where rotation starts
        while left < n and arr[left] <= arr[(left + 1) % n]:
            left += 1
        
        # Adjust pointers considering the rotation
        if left == n:
            left = 0
        else:
            right = (n - 1) % left
        
        while left != right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left = (left + 1) % n
            else:
                right = (n + right - 1) % n
        
        return False

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))