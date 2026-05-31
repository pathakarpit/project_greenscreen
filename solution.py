# Problem: Transform One String to Another using Minimum Number of Given Operation
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/

class Solution:
    def solve(self, s1, s2):
        if len(s1) != len(s2):
            return -1
        
        # Count the frequency of each character in both strings
        count_s1 = {}
        count_s2 = {}
        
        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1
        for char in s2:
            count_s2[char] = count_s2.get(char, 0) + 1
        
        # Check if the two strings are not anagrams of each other
        if count_s1 != count_s2:
            return -1
        
        # If they are already equal, no operations are needed
        if s1 == s2:
            return 0
        
        # Brute force approach to find the minimum number of operations
        min_operations = float('inf')
        for i in range(len(s1)):
            current_operations = 0
            flag = True
            for j in range(len(s2)):
                if s1[j] != s2[(i + j) % len(s1)]:
                    current_operations += 1
                # If the character does not match and cannot be matched, break early
                if current_operations >= min_operations:
                    flag = False
                    break
            if flag:
                min_operations = min(min_operations, current_operations)
        
        return min_operations

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))