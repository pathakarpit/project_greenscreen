class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to keep track of opening brackets
        stack = []
        
        # Define a mapping for closing brackets to their corresponding opening brackets
        # This allows us to quickly check if a closing bracket matches the top of the stack
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Iterate through each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Get the top element from the stack. If the stack is empty,
                # assign a dummy value (e.g., '#') which won't match any opening bracket.
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the expected opening bracket
                # for the current closing bracket.
                if mapping[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
                
        # After iterating through all characters, if the stack is empty,
        # it means all opening brackets have been correctly closed.
        # Otherwise, there are unclosed opening brackets.
        return not stack