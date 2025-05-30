# 일정 금액 지불 시 10일 동안 회원 자격 부여
# 회원을 대상으로 매일 한 가지 제품을 할인하는 행사 진행.
# 할인하는 제품 -> 하루에 1개씩 구매 가능
# 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속 일치 -> 회원가입.

# 바나나 3, 사과 2, 쌀 2, 돼지고기 2, 냄비 1
# 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나

# 정현이가 원하는 제품을 나타내는 문자열 배열 -> want
# 정현이가 원하는 제품의 수량을 나타내는 정수 배열 -> number
# XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 -> discount

# 1 <= want = number <= 10
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

def solution(want, number, discount):
    answer = 0
    from collections import Counter
    want_c = Counter({want[i]:number[i] for i in range(len(want))})
    for i in range(0, len(discount) - 9 if len(discount) >= 10 else 1):
        discount_c = Counter(discount[i:i+10])
        result_c = want_c - discount_c
        if len(result_c) < 1:
            answer += 1    
    return answer

solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])