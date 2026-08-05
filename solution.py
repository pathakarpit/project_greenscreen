# Problem: Merge Sorted Arrays using O(1) Space
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/

class Solution:
    def solve(self, a, b):
        # Initialize two pointers for each array
        i, j = 0, 0
        
        # Initialize two lists to store the merged result and one extra list to store remaining elements after merge
        merged_list = []
        remaining_a = []
        remaining_b = []
        
        # Use two pointers to traverse both arrays until one of them is exhausted
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged_list.append(a[i])
                i += 1
            else:
                merged_list.append(b[j])
                j += 1
        
        # If there are remaining elements in either array, add them to the respective list
        while i < len(a):
            remaining_a.append(a[i])
            i += 1
        while j < len(b):
            remaining_b.append(b[j])
            j += 1
        
        # Return the merged list and the two remaining lists if any
        return merged_list, remaining_a + remaining_b

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))