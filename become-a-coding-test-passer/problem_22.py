def solution(record):
    name_nickname_map = {}
    answer = []
    for sentence in record[::-1]:
        stc_list = sentence.split(" ")
        if stc_list[0] in ['Change', 'Enter'] and stc_list[1] not in name_nickname_map:
            name_nickname_map[stc_list[1]] = stc_list[2]
    
    for sentence in record:
        stc_list = sentence.split(" ")
        if stc_list[0] == 'Enter':
            answer.append(f"{name_nickname_map[stc_list[1]]}님이 들어왔습니다.")
        elif stc_list[0] == 'Leave':
            answer.append(f"{name_nickname_map[stc_list[1]]}님이 나갔습니다.")
    return answer