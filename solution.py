# Problem: Partition of Set into K Subsets with Equal Sum
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/

class Solution:
    def solve(self, arr, k):
        n = len(arr)
        if k == 1: return True
        total_sum = sum(arr)
        if total_sum % k != 0: return False
        target = total_sum // k
        
        # Sort the array in descending order to try larger numbers first
        arr.sort(reverse=True)
        
        def can_partition(start, subset_sums, used):
            if start == n:
                for sum in subset_sums:
                    if sum != target: return False
                return True
            
            for i in range(len(subset_sums)):
                if subset_sums[i] + arr[start] <= target:
                    subset_sums[i] += arr[start]
                    used[start] = True
                    if can_partition(start + 1, subset_sums, used): return True
                    subset_sums[i] -= arr[start]
                    used[start] = False
            return False
        
        subset_sums = [0] * k
        used = [False] * n
        return can_partition(0, subset_sums, used)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))