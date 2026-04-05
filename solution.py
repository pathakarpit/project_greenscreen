# Problem: Valid Palindrome
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def solve(self, sentence):
        # Remove all non-alphabetic characters and convert to lowercase
        cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalpha())
        
        # Use two pointers to check if the cleaned sentence is a palindrome
        left, right = 0, len(cleaned_sentence) - 1
        while left < right:
            if cleaned_sentence[left] != cleaned_sentence[right]:
                return False
            left += 1
            right -= 1
        return True

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))