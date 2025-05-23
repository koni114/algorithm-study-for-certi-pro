def solution(s):
    from collections import deque
    d, s_len = deque(s), len(s)
    check_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    def check_d(d):
        tmp_d = deque()
        for s in d:
            if s in ['(', '{', '[']:
                tmp_d.append(s)
            else:
                if len(tmp_d) < 1 or check_dict[s] != tmp_d[-1]:
                    return 0
                else:
                    tmp_d.pop()
        if len(tmp_d) >= 1:
            return 0
        else:
            return 1
    answer = 0
    while s_len >= 1:
        answer += check_d(d)
        d.rotate(-1)
        s_len -= 1
        
    return answer


solution(s="}}}")


from collections import deque
d = deque([1, 2, 3])
d.pop()