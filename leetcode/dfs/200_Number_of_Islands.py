from typing import List

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
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
                 if 0 <= next_m < M and 0 <= next_n < N and grid[next_m][next_n] == "1" and check[next_m][next_n] == "0":
                     recursive_dfs(next_m, next_n, check)
        
        results = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == "1" and check[m][n] == "0":
                    results += 1
                    recursive_dfs(m, n, check)
        
        return results

s = Solution()
print(s.numIslands(grid))
        
        