# Problem: Inversion of Array
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, inv_left = self.merge_sort(arr[:mid])
        right, inv_right = self.merge_sort(arr[mid:])
        
        merged, inv_split = self.merge_and_count(left, right)
        return merged, inv_left + inv_right + inv_split
    
    def merge_and_count(self, left, right):
        merged = []
        i = j = inv_count = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_count += len(left) - i
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inv_count
    
    def solve(self, arr):
        _, count = self.merge_sort(arr)
        return count

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))