from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        
        def recursive()