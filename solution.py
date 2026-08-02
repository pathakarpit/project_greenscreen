# Problem: find common elements three sorted arrays
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/

class Solution:
    def solve(self, arr1, arr2, arr3):
        from collections import Counter
        
        # Count the occurrences of each element in all three arrays
        count1 = Counter(arr1)
        count2 = Counter(arr2)
        count3 = Counter(arr3)
        
        # Find common elements by intersecting counts
        common_count = count1 & count2 & count3
        
        # Convert the result back to a sorted list of keys (common elements)
        return sorted(list(common_count.elements()))

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))