from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def recursive_dfs(arr, indx, k):
            if k == target:
                