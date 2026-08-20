# Problem: Crossword-Puzzle
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/crossword-puzzle/problem

class Solution:
    def solve(self, grid, words):
        rows = len(grid)
        cols = len(grid[0])
        words_list = words.split(';')
        
        # Helper function to check if placing a word at (r, c) is valid
        def can_place(word, r, c):
            for i in range(len(word)):
                if grid[r][c+i] != '-' and grid[r][c+i] != word[i]:
                    return False
            return True
        
        # Helper function to place a word at (r, c)
        def place_word(word, r, c):
            for i in range(len(word)):
                if grid[r][c+i] == '-':
                    grid[r][c+i] = word[i]
        
        # Helper function to remove a word from (r, c)
        def remove_word(word, r, c):
            for i in range(len(word)):
                if grid[r][c+i] == word:
                    grid[r][c+i] = '-'
        
        # Try to place each word in the grid
        for word in words_list:
            placed = False
            for r in range(rows):
                for c in range(cols - len(word) + 1):
                    if can_place(word, r, c):
                        place_word(word, r, c)
                        if self.solve(grid, words_list[1:]):
                            return True
                        remove_word(word, r, c)
            for r in range(rows - len(word) + 1):
                for c in range(cols):
                    if can_place(word, r, c):
                        place_word(word, r, c)
                        if self.solve(grid, words_list[1:]):
                            return True
                        remove_word(word, r, c)
            # If the word cannot be placed, it means we need to backtrack
            return False
        
        # Check if all words are placed correctly
        for word in words_list:
            found = False
            for r in range(rows):
                for c in range(cols - len(word) + 1):
                    if can_place(word, r, c) and grid[r][c] == word:
                        found = True
                        break
                if found:
                    break
            if not found:
                return False
        return True

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))