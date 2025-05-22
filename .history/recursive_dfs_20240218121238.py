graph = {
    "1": [2, 3, 4],
    "2": [5]
}

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    
    for