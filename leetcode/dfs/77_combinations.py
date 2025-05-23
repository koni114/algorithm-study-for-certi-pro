from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def recursive_dfs(indx, arr):
            
            if len(arr) == k:
                results.append(arr[:])
                return
            if indx >= n:
                return

            arr.append(indx+1)
            recursive_dfs(indx+1, arr)
            
            arr.pop()
            recursive_dfs(indx+1, arr)
        
        recursive_dfs(0, [])
        return results
    
s = Solution()

test_case = [[4, 2], [1, 1]]

for n, k in test_case:
    print(s.combine(n, k))