# Problem: Maximum Possible Number by doing at most K swaps
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/

class Solution:
    def solve(self, nums, k):
        # Create a dictionary to store the index of each number in the array
        index_map = {}
        
        # Iterate through the array and populate the index map
        for i, num in enumerate(nums):
            index_map[num] = i
        
        # Iterate through the array again to rearrange based on the condition k
        rearranged = []
        for num in nums:
            if (k - num) in index_map and len(rearranged) < len(nums):
                rearranged.append(num)
        
        return rearranged

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))