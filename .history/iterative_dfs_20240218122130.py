from collections import deque

graph = {
    1: []
}

def iterative_dfs(v):
    d = deque([v])
    
    while d:
        curr_v = d.pop()
        for w in graph[curr_v]
    