# 정렬
# 실전 문제2. 성적이 낮은 순서로 학생 출력하기

n = int(input())
info = []
for i in range(n):
    a, b = input().split()
    info.append((a, int(b)))

def grade(info):
    return info[1]

info.sort(key=grade)
for i in info:
    print(i[0], end=' ')
