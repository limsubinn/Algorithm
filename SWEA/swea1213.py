# 1213. String

for _ in range(1, 11):
    t = int(input())
    f = input()
    sentence = input()

    answer = 0
    while f in sentence:
        sentence = sentence.replace(f, '', 1) # 해당 문자열 제거
        answer += 1

    print(f'#{t} {answer}')