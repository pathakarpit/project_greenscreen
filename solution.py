# Problem: Combinational Sum
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/combinational-sum/

class Solution:
    def solve(self, candidates, target):
        def backtrack(start, path, remain):
            if remain == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                backtrack(i + 1, path + [candidates[i]], remain - candidates[i])
        
        candidates.sort()
        result = []
        backtrack(0, [], target)
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))