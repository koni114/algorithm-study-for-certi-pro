from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def recursive_dfs(indx, arr)