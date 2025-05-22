from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        
        
        results = []
        def recursive_dfs(nums, arr=[]):
            if not nums:
                results.append(arr)
            
            for v in nums:
                next_arr = deepcopy(arr)
                next_nums = deepcopy(nums)
                recursive_dfs(next_arr.append(v), next_nums.remove(v))
        
        recursive_dfs(nums)
        return results
        