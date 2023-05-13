n, m = map(int, input().split())
answer = (n * (n-1) * (n-2)) // (3 * 2 * 1) # 모든 경우의 수

array = [set() for _ in range(n+1)] # 최악의 조합을 저장할 리스트
for _ in range(m):
    a, b =map(int, input().split())

    # 나머지 하나 고르는 경우의 수 빼기
    answer -= n-2
    # 이미 기존에 뺀 경우의 수 더하기
    answer += len(array[a] | array[b])

    array[a].add(b)
    array[b].add(a)

print(answer)