from typing import List

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict, deque
        tickets_dict = defaultdict(deque)
        results =[]
        
        for deperature,  arrival in tickets:
            tickets_dict[deperature].append(arrival)
            
        tickets_dict = {key: deque(value_list) for key, value_list in tickets_dict.items()}
            
            
        def recursive_dfs(curr_from, tickets_dict):
            
            if curr_from not in tickets_dict:
                return
            
            results.append(curr_from)
            while tickets_dict[curr_from]:
                next_from = tickets_dict[curr_from].popleft()
                recursive_dfs(next_from, tickets_dict)
        
        recursive_dfs("JFK", tickets_dict)
        
        return results
                
            
s = Solution()
print(s.findItinerary(tickets=tickets))
    