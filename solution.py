# Problem: Rabin-Karp Algorithm for Pattern Searching
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

class Solution:
    def solve(self, T, P):
        # Constants for ASCII values of lowercase English letters
        BASE = 26
        MOD = 10**9 + 7
        
        # Function to compute the hash value of a string from start index with length M
        def compute_hash(s, start, M):
            hash_value = 0
            for i in range(M):
                hash_value = (hash_value * BASE + ord(s[start + i]) - ord('a') + 1) % MOD
            return hash_value
        
        # Compute the pattern and text hashes
        N, M = len(T), len(P)
        if N < M:
            return []
        
        P_hash = compute_hash(P, 0, M)
        T_hashes = [compute_hash(T, i, M) for i in range(N - M + 1)]
        
        # Match the pattern hash with text hashes
        result = []
        for i in range(len(T_hashes)):
            if T_hashes[i] == P_hash:
                result.append(i)
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))