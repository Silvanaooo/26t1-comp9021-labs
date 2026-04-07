class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Count the number of islands in a 2D grid.
        Each island is a group of '1's (land) connected horizontally or vertically.
        Use DFS to explore and mark all cells of each island.

        :param grid: 2D list of '1's and '0's (land and water)
        :return: Number of distinct islands
        """
        nums = 0  # Counter for islands
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Four possible directions (right, left, down, up)
        width = len(grid[0])
        height = len(grid)
        # Keep track of visited cells to avoid recounting
        visited = [[False for _ in range(width)] for _ in range(height)]

        def dfs(x, y):
            """
            Depth-First Search: explore all connected land cells from (x, y).

            This is a *defensive-style* DFS:
              - First check all invalid conditions (out of bounds, water, visited) and return immediately.
              - Then mark the cell as visited (entrance marking).
              - Finally, recursively explore 4 neighbors.
            """
            # --- Base conditions ---
            # Out of grid boundaries
            if x < 0 or y < 0 or x >= height or y >= width:
                return
            # If the current cell is water or already visited, stop recursion
            if grid[x][y] == "0" or visited[x][y]:
                return

            # --- Mark this cell as visited as soon as we enter ---
            # This ensures no repeated visits and prevents infinite recursion
            visited[x][y] = True

            # --- Explore all four directions ---
            # Each recursive call continues the search from a neighboring land cell
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                dfs(next_x, next_y)

        # --- Iterate over all cells ---
        for row in range(height):
            for col in range(width):
                # Found an unvisited land cell → start a new DFS
                if grid[row][col] != "0" and not visited[row][col]:
                    dfs(row, col)  # Explore the whole island
                    nums += 1      # Increment island count once per connected region

        return nums