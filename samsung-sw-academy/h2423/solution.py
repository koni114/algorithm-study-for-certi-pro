from collections import deque
from collections import defaultdict

def init(mH, mW):
    """
    각 테스트 케이스의 처음에 호출된다.
    웅덩이의 세로 방향의 길이 mH 와 가로 방향의 길이 mW 가 주어짐.
    웅덩이 안은 비어있음.
    
    8 <= mH <= 1000 
    10 <= mW <= 200,000
    """
    global H, city, adj_list, box_surface, box_height, box_info
    H = mH
    city = [[] for _ in range(H)]
    adj_list = defaultdict(list)
    box_surface = [0] * mW    # 최상층 정보
    box_height =[H] * mW      # 열 별 높이
    
    # 박스id는 1번부터 시작하므로, 더미값 box_info[0] 에 더미값 넣기
    box_info = [(0, 0, 0, 0)] # (start, end, exitA, exitB)

def dropbox(mId: int, mLen: int, mExitA: int, mExitB: int, mCol: int) -> int:
    """
    박스 하나를 떨어트린 후 멈추는 위치의 행의 번호를 반환.
    박스의 번호는 mId, 각 테스트케이스에서 처음 호출시 1, 그 후로는 1씩 증가하여 주어짐
    박스의 길이는 mLen 이며, 박스를 웅덩이의 열 위치 mCol 에서 떨어트림
    박스 내에서 왼쪽 방향으로 이동 가능한 좌우출구는 박스 내의 0번 위치에 있으며,
    오른쪽 방향으로 이동 가능한 좌우출구는 박스 내의 mLen-1 번 위치에 존재
    상하출구 2개의 박스내 위치는 ExitA, mExitB 로 주어지며, 두 값이 동일하게 주어지는 경우는 없음
    
    주어지는 박스는 웅덩이 내에서 멈춤을 보장. 
    웅덩이의 각 행에 멈춘 박스의 개수는 최대 1,200개
    
    mid: 박스의 고유한 번호 (1 <= mId <= 10,000) 
    mLen: 박스의 길이(5 <= mLen <= mW)
    mExitA: 첫번째 상하출구의 위치( 0 <= mExitA < mLen - 1)
    mExitB: 두번째 상하출구의 위치( 0 <= mExitB < mLen - 1)
    mCol: 박스를 떨어뜨리는 웅덩이의 열의 위치( 0 <= mCol <= mW - mLen )
    """
    # 신규 box 정보 삽입
    start = mCol
    end = mCol + mLen - 1
    exitA = mCol + mExitA
    exitB = mCol + mExitB
    box_info.append((start, end, exitA, exitB))
    
    # 신규 box가 삽입될 높이
    height = min(box_height[start:end + 1]) - 1 # min 값이 최상층 -> 그것보다 하나 위(-1)
    
    # 신규 box 좌, 우 확인
    # 긱 행의 최대 박스 갯수는 1,200 개 이므로, for 문은 1,200 번 이내로 동작 -> 소요시간이 크지 않음
    for box_id in city[height]:
        cnt = 0
        # 좌 연결 확인: 기존 end + 1 == 신규 start 
        # 우 연결 확인: 신규 end + 1 == 기존 start
        if box_info[box_id][1] + 1 == start or end + 1 == box_info[box_id][0]:
            # 연결 list 에 삽입 (양방향)
            adj_list[mId].append(box_id)
            adj_list[box_id].append(mId)
            cnt += 1
        if cnt >= 2:  # 양 옆으로 연결되면 끝.
            break
    
    # 신규 box와 접촉한 box 의 id 를 contact_low 에 저장
    contact_low = set()
    if height != H - 1: # 바닥층이 아닌 경우 진행 
        for idx in range(start, end + 1): # 신규박스에 대해서 열의 순차 탐색
            if box_height[idx] == height + 1: # 신규박스 아래(+1)에 박스 있으면,
                contact_low.add(box_surface[idx]) # 최상층 추가
    
    # 아래 연결 box 확인
    for box_id in contact_low:
        # 신규에서 기존에 있는 곳으로 갈 수 있는지 확인
        if box_info[box_id][0] <= exitA <= box_info[box_id][1] or \
            box_info[box_id][0] <= exitB <= box_info[box_id][1]:
                adj_list[mId].append(box_id)
        
        # 기존에서 신규로 갈 수 있는지 확인
        if start <= box_info[box_id][2] <= end or \
            start <= box_info[box_id][3] <= end:
                adj_list[box_id].append(mId)
    
    # city, box_height, box_surface 정보 업데이트
    city[height].append(mId)
    for idx in range(start, end + 1):
        box_height[idx] = height
        box_surface[idx] = mId
    
    return height

# B:기본 BFS
def explore(mIdA: int, mIdB: int) -> int:
    ret = -1
    visited = [False] * (len(box_info) + 1)
 
    q = deque()
    q.append([mIdA, 0])
    visited[mIdA] = True
 
    while q:
        now_node, now_depth = q.popleft()
        if now_node == mIdB:
            ret = now_depth
            break
 
        for next_node in adj_list[now_node]:
            if visited[next_node]:
                continue
            q.append([next_node, now_depth + 1])
            visited[next_node] = True
    return ret