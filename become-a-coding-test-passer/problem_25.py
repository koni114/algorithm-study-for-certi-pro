# 각 유저는 한 번에 한 명의 유저를 신고할 수 있음.
# - 신고 횟수에 제한은 없음. 서로 다른 유저를 계속해서 신고할 수 있음.
# - 한 유저를 여러 번 신고할 수도 있지만, 유저에 대한 신고 횟수는 1회로 처리.
# k번 이상 신고된 유저는 게시판 이용이 정지되며 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
# - 유저가 신고한 모든 내용을 취합해 마지막에 한꺼번에 게시반 이용 정지를 시키면서 정지 메일을 발송
# - 

# declaration = {}
# mailing = {}

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    
    from collections import defaultdict
    declaration, mailing = defaultdict(dict), defaultdict(dict) 
    
    for r in report:
        reporter, reported_p = r.split(" ")
        declaration[reported_p][reporter] = 1
        
    for reported_p in declaration:
        if len(declaration[reported_p]) >= k:
            for reporter in declaration[reported_p]:
                mailing[reporter][reported_p] = 1
    
    return [len(mailing[id]) for id in id_list]

solution(
    id_list = ["con", "ryan"],
    report = ["ryan con", "ryan con", "ryan con", "ryan con"],
    k = 3
)