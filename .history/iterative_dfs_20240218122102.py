from collections import deque

def iterative_dfs(v):
    d = deque([v])
    d.append(v)
    