# Problem: Print all the Duplicates in the Input String
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

class Solution:
    def solve(self, s):
        from collections import Counter
        
        # Using Hashing method (Counter in Python)
        freq = Counter(s)
        duplicates = [char for char in freq if freq[char] > 1]
        
        result = [[char, freq[char]] for char in duplicates]
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))