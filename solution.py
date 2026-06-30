# Problem: Boyer Moore Algorithm for Pattern Searching
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/

class Solution:
    def solve(self, txt, pat):
        n = len(txt)
        m = len(pat)
        
        if m > n:
            return []
        
        # Precompute the bad character heuristic
        last_occurrence = {char: -1 for char in set(txt)}
        for i in range(n):
            last_occurrence[txt[i]] = i
        
        matches = []
        i = m - 1
        while i < n:
            j = m - 1
            k = i
            while j >= 0 and txt[k] == pat[j]:
                k -= 1
                j -= 1
            
            if j < 0:
                matches.append(k + 1)
                shift = max(1, k - last_occurrence.get(txt[k], -2))
            else:
                shift = max(1, j - last_occurrence.get(txt[k], -2))
            
            i += shift
        
        return matches

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))