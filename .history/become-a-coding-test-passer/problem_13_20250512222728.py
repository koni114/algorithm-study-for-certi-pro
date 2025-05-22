def solution(board, moves):
    from collections import deque
    d = deque([])
    answer = 0
    def check_bomb(d: deque, doll_num: int):
        bomb_num = 0
        while d:
            if d[-1] != doll_num:
                break
            else:
                d.pop()
                tmp_v = 2 if bomb_num == 0 else 1
                bomb_num += tmp_v
        
        if not bomb_num:
            d.append(doll_num)
        
        return d, bomb_num
                
    N = len(board)
    for line_num in moves:
        for i in range(N):
            if board[i][line_num-1]:
                d, bomb_num = check_bomb(d, board[i][line_num-1])
                # print(f"d -> {d}, bomb_num -> {bomb_num}")
                answer += bomb_num
                board[i][line_num-1] = 0
                break

    return answer
 

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])