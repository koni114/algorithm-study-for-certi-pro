def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a = int(a / 2 + 0.5)
        b = int(b / 2 + 0.5)

    return answer

solution(8, 4, 7)