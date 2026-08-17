# Problem: Minimum Swaps to Sort
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

class Solution:
    def solve(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        
        indexed_arr = [(val, idx) for idx, val in enumerate(arr)]
        indexed_arr.sort(key=lambda x: x[0])
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or indexed_arr[i][1] == i:
                continue
            
            cycle_length = 0
            x = i
            while not visited[x]:
                visited[x] = True
                x = indexed_arr[x][1]
                cycle_length += 1
            
            if cycle_length > 1:
                swaps += (cycle_length - 1)
        
        return swaps

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))