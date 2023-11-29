# 프로그래머스 17677: 뉴스 클러스터링 (2018 KAKAO BLIND RECRUITMENT)

def makeList(str):
    array = []
    for i in range(1, len(str)):
        # 문자를 두 글자씩 끊어서 알파벳으로 이루어진 경우 소문자로 저장
        s = str[i-1] + str[i]
        if s.isalpha():
            array.append(s.lower())
    return array

def solution(str1, str2):
    s1 = makeList(str1)
    s2 = makeList(str2)

    # 둘 다 공집합인 경우 자카드 유사도가 1
    if not s1 and not s2:
        return 65536

    intersection = 0 # 교집합의 크기
    union = len(s1) + len(s2) # 합집합의 크기
    for s in s1:
        if s in s2: 
            intersection += 1
            i = s2.index(s)
            s2.pop(i)
    union -= intersection

    return int((intersection / union) * 65536)