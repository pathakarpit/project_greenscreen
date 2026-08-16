# Problem: Allocate Minimum number of Pages
# Difficulty: Hard
# Link: https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

class Solution:
    def solve(self, arr, k):
        if len(arr) < k:
            return -1
        
        def is_possible(mid):
            students = 1
            current_sum = 0
            for pages in arr:
                if pages > mid:
                    return False
                if current_sum + pages <= mid:
                    current_sum += pages
                else:
                    students += 1
                    if students > k:
                        return False
                    current_sum = pages
            return True
        
        left, right = max(arr), sum(arr)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))