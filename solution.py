# Problem: Smallest Window in a String Containing all the Characters of Another String
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

class Solution:
    def solve(self, s1: str, s2: str) -> str:
        from collections import Counter
        
        # If s2 is longer than s1, it's impossible to contain all characters of s2 in s1
        if len(s2) > len(s1):
            return ""
        
        # Count the characters in s2
        s2_count = Counter(s2)
        required = len(s2_count)
        
        # Initialize the window and character count dictionaries
        window_count = {}
        left = 0
        formed = 0
        min_length = float('inf')
        result = ""
        
        for right in range(len(s1)):
            char = s1[right]
            # Update the character count in the window
            if char not in window_count:
                window_count[char] = 0
            window_count[char] += 1
            
            # If the frequency of this character matches its requirement, update formed
            if char in s2_count and window_count[char] == s2_count[char]:
                formed += 1
            
            # Try to minimize the window from the left side
            while left <= right and formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s1[left:right+1]
                
                char_left = s1[left]
                window_count[char_left] -= 1
                if char_left in s2_count and window_count[char_left] < s2_count[char_left]:
                    formed -= 1
                
                left += 1
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))