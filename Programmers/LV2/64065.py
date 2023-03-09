# 프로그래머스 64065: 튜플 (2019 카카오 개발자 겨울 인턴십)

def solution(s):
    # 스트링 분리
    s = s.lstrip("{{").rstrip("}}").split("},{")
    tp = []
    for i in s:
        tp.append(list(map(int, i.split(","))))
    # 원소의 개수가 작은 순으로 정렬
    tp.sort(key = lambda x:len(x))
    
    answer = []
    for i in tp:
        j = list(set(i) - set(answer)) # 중복 원소 제거
        answer.append(j[0])
        
    return answer