# 1. 장르 별로 가장 많이 재생된 노래 2개 -> 베스트 앨범 출시.
# 2. 노래는 고유 번호로 구분. -> 노래를 수록하는 기준은 다음과 같음
# - 속한 노래가 많이 재생된 장르를 먼저 수록
# - 장르 내에서 많이 재생된 노래를 먼저 수록
# - 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래 수록
genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

def solution(genres, plays):
    from collections import Counter, defaultdict
    d = defaultdict(int)
    answer = []
    plays_d = defaultdict(list)
    for i in range(len(genres)):
        d[genres[i]] += plays[i]
        plays_d[genres[i]].append([i, plays[i]])
    
    for plays_key in plays_d:
        plays_d[plays_key] = sorted(plays_d[plays_key], key= lambda x: -x[1])
    
    count_genres_dict = Counter(d)
    for genre, count in count_genres_dict.most_common():
        for idx, _ in plays_d[genre][:2]:
            answer.append(idx)
    return answer


solution(genres=["classic", "pop", "classic", "classic", "pop"],
         plays=[500, 600, 150, 800, 2500])