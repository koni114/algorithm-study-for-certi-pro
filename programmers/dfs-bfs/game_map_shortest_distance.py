maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	

def solution(maps):
    
    from collections import deque
    ax, ay, n, m = [1, -1, 0, 0], [0, 0, 1, -1], len(maps), len(maps[0])
    check = [[0 for _ in range(m)] for _ in range(n)]
    
    check[0][0] = 1 
    
    d = deque([[0, 0, 1]])
    
    while d:
        curr_x, curr_y, step_v = d.pop()
        for idx in range(4):
            next_x, next_y = curr_x + ax[idx], curr_y + ay[idx]
            
            if 0 <= next_x < n and 0 <= next_y < m and check[next_x][next_y] == 0 and maps[next_x][next_y] == 1:
                check[next_x][next_y] = step_v + 1
                d.appendleft([next_x, next_y, step_v + 1])

    answer = -1 if check[n-1][m-1] == 0 else check[n-1][m-1]
    return answer

solution(maps)
