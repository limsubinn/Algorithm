# 프로그래머스 176962: 과제 진행하기

def progress(cur_time, in_progress, next_time, answer):
    while in_progress:
        cur_plan = in_progress.pop()

        # 과제가 끝날 시간
        cur_time += cur_plan[1]

        # 진행 중이던 과제 멈추고 새로운 과제 시작하기
        if cur_time > next_time:
            in_progress.append([cur_plan[0], cur_time - next_time])
            return

        # 과제 끝내기
        answer.append(cur_plan[0])

        # 과제를 끝낸 시각에 새로 시작해야 하는 과제가 있는 경우
        if cur_time == next_time:
            return


def solution(plans):
    # 시간 변환
    for i in range(len(plans)):
        s = plans[i][1].split(":")
        plans[i][1] = int(s[0]) * 60 + int(s[1])
        plans[i][2] = int(plans[i][2])
    # 시작 시간 기준으로 내림차순 정렬
    plans.sort(key=lambda x: -x[1])

    answer = []
    in_progress = []

    cur_plan = plans.pop()
    while plans:
        next_plan = plans.pop()

        # 과제가 끝날 시간
        cur_time = cur_plan[1] + cur_plan[2]

        # 진행 중이던 과제 멈추고 새로운 과제 시작하기
        if cur_time > next_plan[1]:
            in_progress.append([cur_plan[0], cur_time - next_plan[1]])
            cur_plan = next_plan
            continue

        # 과제 끝내기
        answer.append(cur_plan[0])
        cur_plan = next_plan

        # 과제를 끝낸 시각에 새로 시작해야 하는 과제가 있는 경우
        if cur_time == next_plan[1]:
            continue

        # 멈춘 과제 이어서 하기
        progress(cur_time, in_progress, next_plan[1], answer)

    # 남은 과제 순서대로 끝내기
    answer.append(cur_plan[0])
    while in_progress:
        answer.append(in_progress.pop()[0])

    return answer