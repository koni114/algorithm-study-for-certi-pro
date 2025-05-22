def solution(n, k, cmd):
    from collections import deque
    rm_stack = deque([])
    up_list = [i for i in range(-1, n)]
    down_list = [i for i in range(1, n+2)]
    
    for cur_cmd in cmd:
        cur_cmd_list = cur_cmd.split(" ")
        cur_cursor = cur_cmd_list[0]
        if cur_cursor == "D":
            tmp_v = int(cur_cmd_list[1])
            while tmp_v:
                k = down_list[k]
                tmp_v -= 1
            if k >= n:
                k = n - 1
        elif cur_cursor == "U":
            tmp_v = int(cur_cmd_list[1])
            while tmp_v:
                k = up_list[k]
                tmp_v -= 1
            if k < 0:
                k = 0
        elif cur_cursor == "C":
            rm_stack.append(k)
            up_list[k+1] -= 1
            if k > 0:
                down_list[k-1] += 1
            if k == n-1:
                k = up_list[k]
            else:
                k = down_list[k]
        else:
            re_k = rm_stack.pop()
            up_list[re_k+1] =+ 1
            if re_k > 0:
                down_list[re_k-1] -= 1
    
    
    answer = ['O' for _ in range(n)]
    while rm_stack:
        v = rm_stack.pop()
        answer[v] = 'X'
    return "".join(answer)


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
