# Problem: Flattening a linked list
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/flattening-a-linked-list/

class Solution:
    def solve(self, raw_content):
        # Check if the input is valid (contains some content)
        if not raw_content:
            return "Invalid Problem Description"
        
        # Implement a method to extract and analyze the problem statement from raw_content
        # For demonstration purposes, let's assume we are looking for specific keywords or patterns that indicate a coding problem.
        
        # Example logic to identify if the content is related to extracting text:
        if "extract" in raw_content.lower() and "text" in raw_content.lower():
            return "Extract the core problem statement, create three clear input/output examples, define constraints, and remove any solution code from the raw text scraped from a coding website."
        
        # If no specific keywords are found or if there is ambiguity, we can provide an error message:
        return "Invalid Problem Description"

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))