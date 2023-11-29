n = int(input())
array = list(map(int, input().split()))

prefix_sum = [array[0]]
for i in range(1, n): # 누적합
    prefix_sum.append(prefix_sum[i-1] + array[i])

answer = 0
for i in range(1, n-1):
    # 벌 벌 꿀통 -> 벌1 왼쪽 끝, 꿀통 오른쪽 끝, 벌2 위치 i
    answer = max(answer, prefix_sum[n-1] - array[i] - array[0] + prefix_sum[n-1] - prefix_sum[i])
    # 꿀통 벌 벌 -> 꿀통 왼쪽 끝, 벌2 오른쪽 끝, 벌1 위치 i
    answer = max(answer, prefix_sum[i-1] + prefix_sum[n-2] - array[i])
    # 벌 꿀통 벌 -> 벌1 왼쪽 끝, 벌2 오른쪽 끝, 꿀통 위치 i
    answer = max(answer, prefix_sum[i] - array[0] + prefix_sum[n-2] - prefix_sum[i-1])

print(answer)

'''
55점 (n의 크기가 클 때 시간 초과) - 누적합 이용 X

n = int(input())
array = list(map(int, input().split()))

answer = 0
for i in range(1, n-1):
    answer = max(answer, sum(array[1:n]) - array[i] + sum(array[i+1:n]))
    answer = max(answer, sum(array[:i]) + sum(array[:n-1]) - array[i])
    answer = max(answer, sum(array[1:i+1]) + sum(array[i:n-1]))

print(answer)
'''