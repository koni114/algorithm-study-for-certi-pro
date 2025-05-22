def solution(board, moves):
    from collections import deque
    d = deque([])
    def check_bomb(d: deque, doll_num: int):
        bomb_num = 0
        while d:
            if d[-1] != doll_num:
                d.append(doll_num)
                break
            else:
                d.pop()
                tmp_v = 2 if bomb_num == 0 else 1
                bomb_num += tmp_v
        
        return d, bomb_num
                
    N = len(board)
    for line_num in moves:
        for i in range(N):
            if board[line_num][i]:
                check_bomb(d, board[line_num][i])
                board[line_num][i] = 0
                break
                
    answer = 0
    return answer