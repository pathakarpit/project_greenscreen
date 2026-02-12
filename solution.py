# Problem: Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def solve(self, height):
        if not height or len(height) < 2:
            return 0
        
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the area of water trapped between two lines
            width = right - left
            h = min(height[left], height[right])
            water = width * h
            
            # Update the maximum amount of water if necessary
            max_water = max(max_water, water)
            
            # Move the pointer which points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))