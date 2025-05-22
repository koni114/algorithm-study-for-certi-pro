from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def recursive_dfs(arr, indx, k):
            if k == target:
                results.append(arr[:])
                return
            
            if k < target or indx >= len(candidates):
                return
            
            recursive_dfs(arr, indx+1)
            arr.append(candidates[indx])