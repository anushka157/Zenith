#Problem: Number of Islands
#Description

#Given a 2D grid of '1's (land) and '0's (water), count the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

#Classic DFS/BFS problem in graphs

#Medium difficulty, common in coding interviews




def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == '0' or visited[r][c]:
            return
        visited[r][c] = True
        # explore neighbors
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                dfs(r, c)
                count += 1
    return count

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("Number of islands:", num_islands(grid))
