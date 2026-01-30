# Problem: Trapping Rain Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def solve(self, heights):
        if not heights:
            return 0
        
        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area between the two pointers
            current_area = min(heights[left], heights[right]) * (right - left)
            # Update the maximum area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer that points to the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))