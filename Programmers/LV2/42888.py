# 프로그래머스 42888: 오픈채팅방 (2019 KAKAO BLIND RECRUITMENT)

def printMsg(info, name):
    if info[0] == "Enter":
        return name[info[1]] + "님이 들어왔습니다."
    elif info[0] == "Leave":
        return name[info[1]] + "님이 나갔습니다."
    else:
        return

def solution(record):
    # 이름 딕셔너리 {uid: name}
    name = {}
    for i in record:
        i = i.split()
        if i[0] != "Leave":
            name[i[1]] = i[2]
    
    # 해당 메시지 출력
    answer = []
    for i in record:
        info = i.split()[:2]
        msg = printMsg(info, name)

        if msg:
            answer.append(printMsg(info, name))
        
    return answer