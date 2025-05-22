def solution(progresses, speeds):
    from collections import deque
    d_p, d_s = deque(progresses), deque(speeds)
    answer = []
    while d_p:
        for i in range(len(d_p)):
            d_p[i] = d_p[i] + d_s[i]
        deploy_v = 0
        while d_p:
            if d_p[0] >= 100:
                deploy_v += 1
                d_p.popleft()
                d_s.popleft()
            else:
                break
        if deploy_v:
            answer.append(deploy_v)
        
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])