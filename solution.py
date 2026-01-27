# Problem: Search in Rotated Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def solve(self, arr, key):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == key:
                return mid
            
            # If the array is rotated and the left half is sorted
            if arr[left] <= arr[mid]:
                if arr[left] <= key < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the right half is sorted
            else:
                if arr[mid] < key <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))