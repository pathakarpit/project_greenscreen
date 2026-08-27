# Problem: Remove Invalid Parentheses
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/remove-invalid-parentheses/

class Solution:
    def solve(self, s):
        # Function to check if a string has valid parentheses
        def is_valid(str_val):
            count = 0
            for char in str_val:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        # Use a queue to perform BFS
        queue = [s]
        visited = set()
        valid_strings = []
        
        while queue:
            current_str = queue.pop(0)
            if is_valid(current_str):
                valid_strings.append(current_str)
            
            # If we have found a valid string, no need to generate more substrings
            if not queue and not valid_strings:
                for i in range(len(current_str)):
                    if current_str[i] == '(' or current_str[i] == ')':
                        new_str = current_str[:i] + current_str[i+1:]
                        if new_str not in visited:
                            queue.append(new_str)
                            visited.add(new_str)
        
        return valid_strings[0] if valid_strings else ""

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))