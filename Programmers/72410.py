# 프로그래머스 72410: 신규 아이디 추천 (2021 KAKAO BLIND RECRUITMENT)

def solution(new_id):
    # 1단계 -> 소문자 만들기 
    new_id = new_id.lower()

    # 2단계 -> 예외 문자 제거 
    exc = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in exc:
        if i in new_id:
            new_id = new_id.replace(i, '')

    # 3단계 -> 연속 . 제거 
    ### 내 코드
    i = 1
    while True:
        if len(new_id) < 2:
            break
        if new_id[i-1] == '.' and new_id[i] == '.':
            new_id = new_id[:i-1] + new_id[i:]
        else:
            i += 1
        if i >= len(new_id):
            break
    ### 참고 코드 
    # while '..' in new_id:
    #     new_id = new_id.replace('..', '.')

    # 4단계 -> 처음과 끝의 . 제거 
    new_id = new_id.strip('.')

    # 5단계 -> 빈 문자열에 a 대입
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계 -> 길이 15자 이후 제거 & 끝의 . 제거
    new_id = new_id[0:15].rstrip('.')

    # 7단계 -> 길이 2자 이하일 때 마지막 문자를 길이가 3이 될 때까지 반복해서 붙이기
    while True:
        if len(new_id) > 2:
            break
        new_id = new_id + new_id[-1]

    return new_id