# Problem: Subarray Sum Divisible K
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/longest-subarray-sum-divisible-k/

class Solution:
    def solve(self, arr, k):
        n = len(arr)
        if n == 0:
            return 0
        
        # Hash map to store the first index of each remainder
        rem_index = {}
        rem_index[0] = -1  # Initialize with a remainder of 0 at index -1 (no elements considered yet)
        
        cumulative_sum = 0
        max_length = 0
        
        for i in range(n):
            cumulative_sum += arr[i]
            current_remainder = cumulative_sum % k
            
            # If the remainder is negative, we need to adjust it by adding k
            if current_remainder < 0:
                current_remainder += k
            
            # Check if this remainder has been seen before
            if current_remainder in rem_index:
                # Calculate the length of the subarray ending at index i
                length = i - rem_index[current_remainder]
                max_length = max(max_length, length)
            else:
                # Store the first occurrence of this remainder
                rem_index[current_remainder] = i
        
        return max_length

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))