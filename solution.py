# Problem: Longest Common Prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def solve(self, arr):
        if not arr:
            return ""
        
        # Find the shortest string in the array
        min_len = min([len(s) for s in arr])
        
        # Initialize the prefix as an empty string
        prefix = ""
        
        # Check each character position up to the length of the shortest string
        for i in range(min_len):
            char = arr[0][i]  # Get the character from the first string at position i
            
            # Check if this character is the same in all strings
            if all(s[i] == char for s in arr):
                prefix += char  # If so, add it to the prefix
            else:
                break  # Stop checking if we find a mismatch
        
        return prefix

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))