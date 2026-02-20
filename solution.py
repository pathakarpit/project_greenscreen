# Problem: Given an Array of Numbers Arrange the Numbers to Form the Biggest Number
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

class Solution:
    def solve(self, nums):
        # Helper function to compare two numbers when concatenated
        def custom_compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Remove non-digit characters and sort the numbers based on custom comparison
        nums = [''.join(filter(str.isdigit, num)) for num in nums]
        nums.sort(key=lambda x: int(x), reverse=True)
        
        # Concatenate the sorted numbers
        largest_num = ''.join(nums)
        
        # Handle leading zeroes by converting to integer and back to string
        if len(largest_num) > 1 and largest_num[0] == '0':
            return '0'
        else:
            return largest_num

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))