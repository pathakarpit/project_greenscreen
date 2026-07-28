# Problem: counting sort
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/counting-sort/

class Solution:
    def solve(self, nums):
        if not nums:
            return []
        
        max_value = max(nums)
        min_value = min(nums)
        
        # Create a count array to store the count of each element
        count_array = [0] * (max_value - min_value + 1)
        
        # Populate the count array with counts from the input array
        for num in nums:
            count_array[num - min_value] += 1
        
        # Modify the count array to contain cumulative counts
        for i in range(1, len(count_array)):
            count_array[i] += count_array[i - 1]
        
        # Create a sorted output array using the count array and input array
        sorted_nums = [0] * len(nums)
        for num in reversed(nums):
            index = count_array[num - min_value] - 1
            sorted_nums[index] = num
            count_array[num - min_value] -= 1
        
        return sorted_nums

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))