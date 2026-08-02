# Problem: majority element
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/majority-element/

class Solution:
    def solve(self, arr):
        candidate = None
        count = 0
        
        # Find the potential candidate for majority element
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        
        # Verify that the candidate is indeed a majority element
        count = sum(1 for num in arr if num == candidate)
        return candidate if count > len(arr) / 2 else -1

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))