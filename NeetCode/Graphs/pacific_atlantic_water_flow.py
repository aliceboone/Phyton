'''There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
'''


from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        can_reach_pac = [[False] * n for _ in range(m)]
        can_reach_atl = [[False] * n for _ in range(m)]

        # DFS from cells on the first row and column
        for i in range(m):
            self.dfs(heights, i, 0, can_reach_pac)
            self.dfs(heights, i, n - 1, can_reach_atl)
        for j in range(n):
            self.dfs(heights, 0, j, can_reach_pac)
            self.dfs(heights, m - 1, j, can_reach_atl)

        # Find cells that can flow to both oceans
        res = []
        for i in range(m):
            for j in range(n):
                if can_reach_pac[i][j] and can_reach_atl[i][j]:
                    res.append([i, j])

        return res

    def dfs(self, heights, i, j, can_reach):
        can_reach[i][j] = True
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if ni < 0 or ni >= m or nj < 0 or nj >= n:
                continue
            if can_reach[ni][nj] or heights[ni][nj] < heights[i][j]:
                continue
            self.dfs(heights, ni, nj, can_reach)


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
solution = Solution()
print(solution.pacificAtlantic(heights)) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
