# Problem: Group Anagrams
# Difficulty: Medium
# Link: https://leetcode.com/problems/group-anagrams/

class Solution:
    def solve(self, words):
        anagrams = {}
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        
        return list(anagrams.values())

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))