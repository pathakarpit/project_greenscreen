class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to keep track of open brackets
        stack = []
        
        # Define a dictionary to map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        # Iterate over each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Get the top element from the stack. If the stack is empty, assign a dummy value
                # This handles cases like "]" where there's no opening bracket
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element is the correct opening bracket for the current closing bracket
                # If they don't match, or if stack was empty (top_element was '#'), it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
                
        # After iterating through all characters, if the stack is empty,
        # all opening brackets have been matched and closed correctly.
        # Otherwise, there are unmatched opening brackets.
        return not stack