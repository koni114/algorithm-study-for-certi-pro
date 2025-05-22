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

def iterative_dfs(v):
    d, discovered = deque([v]),  [v]

    while d:
        curr_v = d.pop()
        for w in graph[curr_v]:
            if w not in discovered
    