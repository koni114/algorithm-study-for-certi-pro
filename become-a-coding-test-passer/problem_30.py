def solution(maps):
    from collections import deque
    next_points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = 0
    x_len, y_len = len(maps), len(maps[0])
    
    for i in range(x_len):
        for j in range(y_len):
            if maps[i][j] == 'S':
                start_point = (i, j)
            elif maps[i][j] == 'L':
                lever_point = (i, j)
            elif maps[i][j] == 'E':
                end_point = (i, j)
    
    def bfs(d: deque, end_point: tuple):
        checked = [[False] * y_len for _ in range(x_len)]
        checked[d[0][0]][d[0][1]] = True
        while d:
            curr_x, curr_y, curr_v = d.popleft()
            if (curr_x, curr_y) == end_point:
                return curr_v
            for ax, ay in next_points:
                next_x, next_y = curr_x + ax, curr_y + ay
                if 0 <= next_x < x_len and 0 <= next_y < y_len and maps[next_x][next_y] not in ['X'] and not checked[next_x][next_y]:
                    checked[next_x][next_y] = True
                    d.append((next_x, next_y, curr_v+1))
        return -1
    
    d = deque([(start_point[0], start_point[1], 0)])
    results_v = bfs(d, lever_point)
    if results_v == -1:
        return -1
    else:
        answer += results_v
    
    d = deque([(lever_point[0], lever_point[1], 0)])
    results_v = bfs(d, end_point)
    if results_v == -1:
        return -1
    else:
        answer += results_v
        
    return answer