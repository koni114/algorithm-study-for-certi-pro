from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def recursive_dfs(arr, indx, k):
            if k == target:
                print(arr)
                results.append(arr[:])
                return
            
            if k > target or indx >= len(candidates):
                return
            
            recursive_dfs(arr[:], indx+1, k)
            curr_v = candidates[indx]
            
            arr.append(curr_v)
            
            recursive_dfs(arr[:], indx, k + curr_v)
            recursive_dfs(arr[:], indx+1, k + curr_v)
            
        recursive_dfs([], 0, 0)
        return results

s = Solution()

test_case = [
    [[2,3,6,7], 7],
    [[2,3,5], 8],
    [[2], 1]
]

for candidates, target in test_case:
    print(s.combinationSum(candidates, target))
