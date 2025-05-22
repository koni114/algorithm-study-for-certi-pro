from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        
        
        results = []
        def recursive_dfs(nums, arr=[]):
            if not nums:
                results.append(arr)
                return
            
            for v in nums:
                next_arr = deepcopy(arr)
                next_nums = deepcopy(nums)
                
                next_arr.append(v)
                next_nums.remove(v)
                
                recursive_dfs(nums=next_nums, arr=next_arr)
        
        recursive_dfs(nums)
        return results
    
s = Solution()

nums_list = [[1,2,3], [0,1], [1]]
for nums in nums_list:
    print(s.permute(nums))


## 정답지
def permute(nums: List[int]) -> List[List[int]]:
    results = []