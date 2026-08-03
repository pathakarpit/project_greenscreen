# Problem: count triplets with sum smaller that a given value
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

class Solution:
    def solve(self, arr, target):
        arr.sort()
        count = 0
        n = len(arr)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    count += 1
                    # Skip duplicates for the second and third elements in the triplet
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return count

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))