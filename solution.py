# Problem: Longest Repeating Character Replacement
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def solve(self, s, k):
        char_count = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] not in char_count:
                char_count[s[right]] = 0
            char_count[s[right]] += 1
            
            while (right - left + 1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))