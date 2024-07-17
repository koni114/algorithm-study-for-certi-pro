n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def solution(n, computers):
    
    from collections import defaultdict, deque
    from typing import List
    graph = defaultdict(list)
    answer = 0
    
    for idx, edge in enumerate(computers):
        for edge_idx, v in enumerate(edge):
            if v == 1 and edge_idx != idx:
                graph[idx].append(edge_idx)
    
    discovered = []
    
    def dfs(v, discovered: List):
        
        discovered.append(v)
        d = deque([v])
        
        while d:
            tmp = d.pop()
            for w in graph[tmp]:
                if w not in discovered:
                    d.append(w)
                    discovered.append(w)
        
        return discovered
    
    
    for i in range(n):
        if i not in discovered:
            answer += 1
            discovered = dfs(i, discovered)
    
    return answer


print(solution(n, computers))