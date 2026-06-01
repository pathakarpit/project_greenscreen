# Problem: Minimum Window Substring
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def solve(self, s1, s2):
        from collections import Counter
        
        # Count characters in s2
        target = Counter(s2)
        required = len(target)
        
        # Initialize the window's character counters
        window_counts = {}
        
        left, right = 0, 0
        formed = 0
        min_length = float('inf')
        result = ""
        
        while right < len(s1):
            char = s1[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in target and window_counts[char] == target[char]:
                formed += 1
                
            while left <= right and formed == required:
                # Update the result
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s1[left:right+1]
                    
                # Move the left pointer to shrink the window
                left_char = s1[left]
                window_counts[left_char] -= 1
                
                if left_char in target and window_counts[left_char] < target[left_char]:
                    formed -= 1
                    
                left += 1
            
            right += 1
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))