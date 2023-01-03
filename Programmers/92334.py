# 프로그래머스 92334: 신고 결과 받기 (2022 KAKAO BLIND RECRUITMENT)

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report = set(report) # 중복 제거 

    dic = {} # 딕셔너리
    for i in range(len(id_list)):
        dic[id_list[i]] = []

    for i in report:
        dic[i.split()[1]].append(i.split()[0])

    for i in id_list:
        if len(dic[i]) >= k:
            for j in dic[i]:
                answer[id_list.index(j)] += 1

    return answer