# Professor's Analysis: Knight Tour

## Time Complexity Analysis
The time complexity of this algorithm is O(N), where N is the total number of squares on the chessboard (8x8 = 64). This is because we visit each square once.

*   The loop in `solve_util` runs N times, which is O(N).
*   Inside the loop, dictionary lookup (`if x in dict`) takes O(1) time on average.
*   Therefore, N * O(1) = O(N).

## Space Complexity Analysis
The space complexity of this algorithm is O(N), where N is the total number of squares on the chessboard. We use a 2D list (or matrix) to store at most N elements.

## Step-by-Step Reconstruction Logic

### Initialization
*   The `Solution` class has an initializer method (`__init__`) that:
    *   Initializes an instance variable `moves`, which is a list of tuples representing the possible moves on the chessboard.
    *   Initializes an instance variable `board_size`, which is set to 8 (the size of the chessboard).
    *   Initializes an instance variable `solution`, which is a 2D list filled with -1 values, representing the solution matrix.

### Solution Existence Check
*   The `solve` method checks if a solution exists by calling the `solve_util` method with the starting position (0, 0) and move count 0.
*   If a solution exists, it prints the solution matrix using the `print_solution` method and returns True.

### Utility Method: Solve Util
*   The `solve_util` method takes three parameters:
    *   x: the current x-coordinate on the chessboard (integer)
    *   y: the current y-coordinate on the chessboard (integer)
    *   move_count: the current move count (integer)
*   It checks if the move count is equal to the total number of squares on the board (`board_size * board_size`). If so, it returns True.
*   Otherwise, it iterates over all possible moves:
    *   For each move, it calculates the next x and y coordinates using the `moves` list.
    *   It checks if the new position is valid (i.e., within the chessboard bounds) and has not been visited before (`solution[x][y] == -1`).
    *   If the new position is valid, it marks it as visited by setting `solution[next_x][next_y] = move_count`.
    *   It recursively calls `solve_util` with the updated position and incrementing move count.
    *   If a solution is found, it returns True.
    *   If no solution is found after trying all moves, it backtracks by resetting the visited mark (`solution[next_x][next_y] = -1`) and returns False.

### Solution Printing
*   The `print_solution` method simply prints each row of the `solution` matrix.
