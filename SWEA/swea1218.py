# 1218. 괄호 짝짓기

for t in range(1, 11):
    n = int(input())
    s = input()

    while True:
        # 괄호 제거
        if '{}' in s:
            s = s.replace('{}', '')
        elif '()' in s:
            s = s.replace('()', '')
        elif '[]' in s:
            s = s.replace('[]', '')
        elif '<>' in s:
            s = s.replace('<>', '')
        # 더이상 제거할 괄호가 없으면 종료
        else:
            break

    # 문자열이 남아있는 경우 - 괄호의 짝이 맞지 않음
    if s:
        answer = 0
    # 문자열이 남아있지 않은 경우 - 모든 괄호의 짝이 맞음
    else:
        answer = 1
    print(f'#{t} {answer}')