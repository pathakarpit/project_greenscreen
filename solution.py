# Problem: Kth-Largest Element in an Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def solve(self, arr, k):
        def partition(left, right, pivot_index):
            pivot_value = arr[pivot_index]
            # Move pivot to end
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            store_index = left
            for i in range(left, right):
                if arr[i] < pivot_value:
                    arr[store_index], arr[i] = arr[i], arr[store_index]
                    store_index += 1
            # Move pivot to its final place
            arr[right], arr[store_index] = arr[store_index], arr[right]
            return store_index
        
        def select(left, right, k_smallest):
            if left == right:
                return arr[left]
            # Choose a pivot index randomly
            pivot_index = left + (right - left) // 2
            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                return arr[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)
        
        n = len(arr)
        if k > 0 and k <= n:
            return f"The {k}th largest element is: {select(0, n - 1, k - 1)}"
        else:
            raise ValueError("Invalid input")

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))