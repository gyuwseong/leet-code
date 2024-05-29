class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    sr, sc = row + dr, col + dc
                    if (sr in range(rows) and (sc in range(cols)) and (grid[sr][sc] == "1") and ((sr, sc) not in visit)):
                        q.append((sr, sc))
                        visit.add((sr, sc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    bfs(r, c)
        return islands
