from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def recursive_dfs(arr, indx, k):
            print(f"arr -> {arr}, indx -> {indx}, k -> {k}")
            if k > target or indx >= len(candidates):
                return

            if k == target:
                results.append(arr[:])
                return
            
            recursive_dfs(arr[:], indx+1, k)  # pass
            curr_v = candidates[indx]
            
            next_arr = arr[:]
            next_arr.append(curr_v)
            
            
            recursive_dfs(next_arr, indx, k + curr_v)   # add + no pass
            recursive_dfs(next_arr, indx+1, k + curr_v) # add + pass
            
        recursive_dfs([], 0, 0)
        return results

s = Solution()

test_case = [
    [[2,3,6,7], 7],
    # [[2,3,5], 8],
    [[1, 2], 3]
]

for candidates, target in test_case:
    print(s.combinationSum(candidates, target))
