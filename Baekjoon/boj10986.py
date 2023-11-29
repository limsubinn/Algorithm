# m으로 나눴을 때 두 수의 나머지가 동일하다면, 빼기 연산 후 나머지 0
# 따라서 나머지가 같은 2개를 뽑으면 된다.

n, m = map(int, input().split())
num = list(map(int, input().split()))

temp = 0 #
remainder = [0] * m

for i in range(n):
    temp += num[i] # 누적합
    remainder[temp % m] += 1 # 인덱스 별로 나머지의 개수 저장

answer = remainder[0]
for i in remainder:
    answer += i * (i-1) // 2 # 2개를 뽑는 경우의 수 (조합)

print(answer)