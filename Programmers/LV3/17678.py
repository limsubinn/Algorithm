# 프로그래머스 17678: 셔틀버스 (2018 KAKAO BLIND RECRUITMENT)

def time_to_str(t): # 시간을 문자열로 변환
    hh = str(t // 60)
    mm = str(t % 60)
    return hh.zfill(2) + ':' + mm.zfill(2)

def solution(n, t, m, timetable):
    # timetable 분 단위로 변환 후 정렬
    time = []
    for i in timetable:
        i = i.split(":")
        time.append(int(i[0]) * 60 + int(i[1]))
    time.sort(reverse = True)

    # 버스 출발 시간 분 단위로 뽑아내기
    bus = [540]
    start = 540
    for i in range(n-1):
        start += t
        bus.append(start)

    # 마지막 셔틀을 제외하고 셔틀에 승객 태우기 (남은 승객 -> time)
    for i in range(len(bus)-1):
        cnt = 0
        timetable = time[::-1]
        for j in timetable:
            if j > bus[i]:
                break
            if cnt == m:
                break
            time.pop()
            cnt += 1

    # 마지막 셔틀에 승객 태우기
    b = bus.pop()
    timetable = time[::-1]
    for i in range(m-1): # (최대 크루 수 - 1)번 수행
        # 더이상 남은 승객을 태울 수 없는 경우, 마지막 셔틀 시간 리턴
        if timetable[i] > b:
            return time_to_str(b)
        # 더이상 남은 승객이 없을 경우, 마지막 셔틀 시간 리턴
        if not time:
            return time_to_str(b)
        # 승객을 태울 수 있는 경우
        time.pop()

    # 더이상 남은 승객이 없을 경우
    if not time:
        return time_to_str(b)
    

    t = time.pop() # 다음 순서 승객
    # 셔틀에 승객을 태울 수 있을 경우, (승객-1) 시간 리턴
    if t <= b:
        return time_to_str(t-1)
    # 셔틀에 승객을 태울 수 없을 경우, 마지막 셔틀 시간 리턴
    return time_to_str(b)