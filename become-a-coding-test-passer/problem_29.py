enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]


def solution(enroll, referral, seller, amount):
    from collections import defaultdict
    import math
    d = defaultdict(dict)
    d['center'] = {'parent_name': None, 'total_cost': 0}
    results_cost = []
    
    for idx, name in enumerate(enroll):
        d[name]['parent_name'] = referral[idx] if referral[idx] != "-" else 'center'
        d[name]['total_cost'] = 0
        
    for idx, name in enumerate(seller):
        total_cost = amount[idx] * 100
        curr_name = name
        while True:
            if d[curr_name]['parent_name']:
                if math.floor(total_cost * 0.1) == 0:
                    d[curr_name]['total_cost'] += total_cost
                    break
                else:
                    upper_cost = math.floor(total_cost * 0.1)
                    d[curr_name]['total_cost'] += (total_cost - upper_cost)
                    total_cost = upper_cost
                    curr_name = d[curr_name]['parent_name']
            else:
                break
            
    for name in enroll:
        results_cost.append(d[name]['total_cost'])
    return results_cost
        
            
solution(
    enroll=enroll,
    referral=referral,
    seller=seller,
    amount=amount
)
