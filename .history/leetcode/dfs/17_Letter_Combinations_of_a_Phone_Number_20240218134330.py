from typing import List
from collections import deque
from copy import deepcopy

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            
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
            for c in num_to_str[int(curr_char)]:
                next_digits = deepcopy(digits)
                recursive_dfs(word + c, next_digits)
                
        recursive_dfs("", digits)
        return results

digits = "2"
s = Solution()
print(s.letterCombinations(digits))
                
