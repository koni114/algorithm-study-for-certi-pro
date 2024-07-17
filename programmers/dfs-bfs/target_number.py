numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    
    from collections import deque
    from copy import deepcopy
    d = deque(numbers)
    global results
    results = 0
    
    def dfs(s, d, total):
        global results
        tmp_d = deepcopy(d)
        if not tmp_d:
            if total == target:
                results += 1
            return
        
        tmp = tmp_d.popleft()
        
        dfs(s+"+"+str(tmp), d=tmp_d, total = total + tmp)
        dfs(s+"-"+str(tmp), d=tmp_d, total = total - tmp)
    
    dfs("", d, 0)
    print(results)
    
solution(numbers, target)