# 프로그래머스 49993: 스킬트리

def solution(skill, skill_trees):
    # 선행 스킬 순서 저장
    dic = {}
    for i, s in enumerate(list(skill)):
        dic[s] = i + 1

    answer = 0
    # 스킬 트리 순회
    for s in skill_trees:
        cnt = 0
        for i in s:
            # 선행 스킬에 저장되어 있는 스킬인 경우
            if i in skill:
                cnt += 1
                # 순서가 맞지 않는 경우
                if cnt != dic[i]:
                    break
        # 순서가 모두 맞는 경우
        else:
            answer += 1

    return answer