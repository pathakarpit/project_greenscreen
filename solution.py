# Problem: Print all Possible Combinations of r Elements in a Given Array of Size n
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/

class Solution:
    def solve(self, arr, r):
        def backtrack(start, path):
            if len(path) == r:
                result.append(path[:])
                return
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))