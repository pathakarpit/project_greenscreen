# Problem: Aggressive Cows
# Difficulty: Hard
# Link: https://www.spoj.com/problems/AGGRCOW/

class Solution:
    def solve(self, stalls, k):
        stalls.sort()
        
        def can_place_cows(min_dist):
            count = 1
            last_placed_cow = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_placed_cow >= min_dist:
                    count += 1
                    last_placed_cow = stalls[i]
                if count == k:
                    return True
            return False
        
        left, right = 0, stalls[-1] - stalls[0]
        while left < right:
            mid = (left + right) // 2
            if can_place_cows(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))