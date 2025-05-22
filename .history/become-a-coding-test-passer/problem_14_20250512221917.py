def solution(n, k, cmd):
    from collections import deque
    rm_stack = deque([])
    up_list = [i - 1 for i in range(n + 2)]
    down_list = [i + 1 for i in range(1, n + 2)]
    
    k += 1
    
    for cur_cmd in cmd:
        cur_cmd_list = cur_cmd.split(" ")
        cur_cursor = cur_cmd_list[0]
        if cur_cursor == "D":
            tmp_v = int(cur_cmd_list[1])
            while tmp_v:
                k = down_list[k]
                tmp_v -= 1
        elif cur_cursor == "U":
            tmp_v = int(cur_cmd_list[1])
            while tmp_v:
                k = up_list[k]
                tmp_v -= 1
        elif cur_cursor == "C":
            rm_stack.append(k)
            up_list[down_list[k]] = up_list[k]
            down_list[up_list[k]] = down_list[k]
            k = up_list[k] if n < down_list[k] else down_list[k]
        else:
            re_k = rm_stack.pop()
            up_list[down_list[re_k]] = re_k
            down_list[up_list[re_k]] = re_k
    
    
    answer = ['O' for _ in range(n)]
    while rm_stack:
        v = rm_stack.pop()
        answer[v] = 'X'
    return "".join(answer)


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])


n = 8
up_list = [i - 1 for i in range(n + 2)]
down_list = [i + 1 for i in range(1, n + 2)]