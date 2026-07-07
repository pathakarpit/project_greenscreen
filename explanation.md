# Professor's Analysis: Given a Matrix of ‘O’ and ‘X’, Replace ‘O’ with ‘X’ if Surrounded by ‘X’

## Time Complexity Analysis
### Big O Notation: O(N)
The loop `for i in range(m):` and `for j in range(n):` run N times each, where N is the total number of elements (m * n). Inside these loops, we perform a dictionary lookup `if board[i][j] == 'O':` which takes O(1) time on average.
Since the loop runs N times and the dictionary lookup takes O(1) time, we multiply them together: N * O(1) = O(N).
### Space Complexity Analysis
The Big O is O(N), as we use a dictionary to store at most N elements.

## Step-by-Step Reconstruction Logic

*   **Initialization**: We initialize two variables `m` and `n` with the lengths of the 2D board.
*   The function `dfs(i, j)` is defined. This function takes two parameters: `i` (row) and `j` (column). It checks if the current cell `(i, j)` is within the boundaries and if its value is `'O'`. If it's not an 'O', we return immediately.
*   We mark the current cell as visited by changing its value to `'T'`.
*   We define a list `directions` which contains all possible directions (up, down, left, right) using tuples `(dx, dy)`.
*   We iterate over each direction and recursively call `dfs(i + dx, j + dy)` if the adjacent cell exists and its value is `'O'`.

### Step 1: Mark all 'O's connected to the boundary with 'T'

*   We initialize two nested loops to iterate over each row and column.
*   Inside the outer loop for rows, we check if the first or last element in the current row (`board[i][0]` or `board[i][n - 1]`) is an `'O'`.
*   If it's an 'O', we call the `dfs(i, 0)` or `dfs(i, n - 1)` function.
*   We perform similar checks for each column using the inner loop.

### Step 2: Convert all remaining 'O's to 'X' and revert 'T' back to 'O'

*   We initialize two nested loops to iterate over each row and column again.
*   Inside the outer loop, we check if the current cell (`board[i][j]`) is an `'O'`.
*   If it's an 'O', we change its value to `'X'`.
*   If the current cell is a `'T'`, we change its value back to `'O'`.
