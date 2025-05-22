from typing import List

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
         M, N = len(grid), len(grid[0])
         AM, AN = [1 , -1, 0, 0], [0, 0, 1, -1]
         check = [["0"] * N for _ in range(M)]
         
         def recursive_dfs(m, n, check):
             check[m][n] = "1"
             for i in range(4):
                 next_m, next_n = m + AM[i], n + AN[i]
                 if 0 <= next_m <= M and 0 <= next_n <= N