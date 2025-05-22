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
         check = [["0"] * N for _ in range(M) ]