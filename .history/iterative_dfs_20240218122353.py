from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: []
}

def iterative_dfs(v, discovered=[]):
    d = deque([v])

    while d:
        curr_v = d.pop()
        discovered.append(curr_v)
        for w in graph[curr_v]:
            if w not in discovered:
                d.append(w)
    
    return discovered

print(iterative_dfs(1))
                
    