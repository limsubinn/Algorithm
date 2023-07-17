n = int(input())
array = list(map(int, input().split()))

array.sort()
result = []

i = 0 # 첫 번째 인덱스
# n이 짝수이면 마지막 인덱스부터 시작
if n % 2 == 0:
    j = n-1
# n이 홀수이면 마지막 인덱스 빼고 시작
else:
    j = n-2
    # 제일 큰 수 따로 저장
    result.append(array[n-1])

# 남은 수 중 가장 작은 수와 가장 큰 수를 더해서 결과값에 저장
while i < j:
    result.append(array[i] + array[j])
    i += 1
    j -= 1

# 최댓값 출력
print(max(result))