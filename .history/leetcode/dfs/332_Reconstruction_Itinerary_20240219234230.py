from typing import List

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        tickets_dict = defaultdict(list)
        results =[]
        
        for deperature,  arrival in tickets:
            tickets_dict[deperature].append(arrival)
            
        def recursive_dfs(curr_from, tickets_dict):
            results.append(curr_from)
            while tickets_dict[curr_from]:
                
            
        