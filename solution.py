# Problem: Searching in an array where adjacent differ by at most k
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/

class Solution:
    def solve(self, arr, x, k):
        for i in range(len(arr)):
            if abs(arr[i] - arr[max(0, i-1)]) <= k and abs(arr[i] - arr[min(len(arr)-1, i+1)]) <= k:
                if arr[i] == x:
                    return f"Element {x} is present at index {i}"
        return "Element not found"

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))