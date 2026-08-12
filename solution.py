# Problem: Find Four Elements that Sum to a Given Value
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/

class Solution:
    def solve(self, vec, target):
        result = []
        n = len(vec)
        
        # Sort the array to use two pointers technique later
        vec.sort()
        
        for i in range(n - 3):
            if i > 0 and vec[i] == vec[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and vec[j] == vec[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = vec[i] + vec[j] + vec[left] + vec[right]
                    
                    if current_sum == target:
                        result.append([vec[i], vec[j], vec[left], vec[right]])
                        
                        # Skip duplicates for left and right pointers
                        while left < right and vec[left] == vec[left + 1]:
                            left += 1
                        while left < right and vec[right] == vec[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))