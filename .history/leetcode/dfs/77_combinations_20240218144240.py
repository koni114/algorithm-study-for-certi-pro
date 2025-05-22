from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def recursive_dfs(indx, arr):
            if len(arr) == k:
                results.append(arr)
                return
            if indx >= n:
                return
            
            arr.append(indx+1)
            recursive_dfs()
            