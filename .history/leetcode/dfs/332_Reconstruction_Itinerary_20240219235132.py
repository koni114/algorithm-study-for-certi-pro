from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict, deque
        tickets_dict = defaultdict(deque)
        results =[]
        
        for deperature,  arrival in tickets:
            tickets_dict[deperature].append(arrival)
            
        tickets_dict = {key: deque(value_list) for key, value_list in tickets_dict.items()}
            
            
        def recursive_dfs(curr_from, tickets_dict):
            results.append(curr_from)
            if curr_from not in tickets_dict:
                return
            while tickets_dict[curr_from]:
                next_from = tickets_dict[curr_from].popleft()
                recursive_dfs(next_from, tickets_dict)
        
        recursive_dfs("JFK", tickets_dict)
        
        return results
                
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]  
s = Solution()
print(s.findItinerary(tickets=tickets))
    