from collections import deque

def iterative_dfs(v):
    d = deque([])
    d.append(v)
    