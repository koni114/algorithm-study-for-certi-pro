def solution(s):
    from collections import deque
    right_d, left_d = deque([]), deque(s)
    while left_d:
        v = left_d.popleft()
        if not right_d:
            right_d.append(v)
        else:
            if right_d[-1] == v:
                right_d.pop()
            else:
                right_d.append(v)
    
    if not len(right_d):
        return 1
    else:
        return 0
        
                
         
    
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer