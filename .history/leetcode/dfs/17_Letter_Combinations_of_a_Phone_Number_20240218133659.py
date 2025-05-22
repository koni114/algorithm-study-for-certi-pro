from typing import List
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_str ={
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        results = []
        digits = deque(digits)
        def recursive_dfs(word, digits):
            if not digits:
                results.append(word)
                return

            curr_char = digits.popleft()
            for c in num_to_char[int(curr_)]
            
                
