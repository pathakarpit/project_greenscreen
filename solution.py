# Problem: Print Subarrays with 0 Sum
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

class Solution:
    def solve(self, nums):
        sums = {}
        curr_sum = 0
        result = []
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum == 0:
                result.append((0, i))
            if curr_sum in sums:
                for start_index in sums[curr_sum]:
                    result.append((start_index + 1, i))
            sums[curr_sum] = sums.get(curr_sum, []) + [i]
        
        if not result:
            print("No subarrays with zero sum found")
        else:
            for start_idx, end_idx in result:
                print(f"Subarray found from Index {start_idx} to {end_idx}")

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))