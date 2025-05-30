
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
course = [2,3,4]
result = ["AC", "ACDE", "BCFG", "CDE"]

def solution(orders, course):
    from itertools import combinations
    from collections import Counter
    answer = []
    for c in course:
        menu = []
        for order in orders:
            comb = combinations(
                sorted(order), c
            )
            menu.extend(list(comb))
        
        counter = Counter(menu)
        if len(counter) != 0 and  max(counter.values()) != 0:
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))
                    
    return sorted(answer)


solution(
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    course = [2,3,4])