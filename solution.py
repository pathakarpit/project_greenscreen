# Problem: Check if Reversing a Sub Array Make the Array Sorted
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/check-reversing-sub-array-make-array-sorted/

class Solution:
    def solve(self, arr):
        n = len(arr)
        if n <= 1:
            return "Yes"
        
        # Find the leftmost element that is out of order
        left = -1
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                left = i
                break
        
        # If no such element is found, the array is already sorted
        if left == -1:
            return "Yes"
        
        # Find the rightmost element that is out of order
        right = n
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                right = i
                break
        
        # Reverse the subarray from left to right and check if it makes the array sorted
        reversed_subarray = arr[:left] + arr[left:right+1][::-1] + arr[right+1:]
        
        # Check if the reversed array is sorted
        for i in range(n - 1):
            if reversed_subarray[i] > reversed_subarray[i + 1]:
                return "No"
        
        return "Yes"

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))