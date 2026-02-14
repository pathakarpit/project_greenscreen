# Problem: Kth - Smallest Element
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

class Solution:
    def solve(self, arr, k):
        # Create a max-heap by pushing negative values of elements into the heap
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)
        
        # Extract the smallest element (which is actually the largest due to negation) k times
        kth_smallest = -heapq.nsmallest(k, max_heap)[-1]
        
        return f"The {k}th smallest element in the array is {kth_smallest}."

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))