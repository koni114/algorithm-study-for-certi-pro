graph = {
    "1": [2, 3, 4],
    "2": [5],
    "3": []
}

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    
    for