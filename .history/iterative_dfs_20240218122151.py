from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
}

def iterative_dfs(v):
    d = deque([v])
    
    while d:
        curr_v = d.pop()
        for w in graph[curr_v]
    