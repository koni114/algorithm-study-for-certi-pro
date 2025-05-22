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
            curr_v = candidates[indx]
            arr.append(curr_v)
            
            recursive_dfs(arr, indx, k - curr_v)
            recursive_dfs(arr, indx+1, k - curr_v)
            
        recursive_dfs([], 0, 0)
        return results

s = Solution()
for candidates, target in test_case:
    print(s.combinationSum(candidates, target))