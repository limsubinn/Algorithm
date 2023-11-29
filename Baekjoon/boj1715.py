import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)  # 최솟값을 꺼내기 위해 우선순위 큐 사용

answer = 0
while len(cards) > 1:
    # 최솟값 두 개 꺼내기
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    # 결과 더하기
    res = a + b
    answer += res

    # 더한 결과값 우선순위 큐에 삽입
    heapq.heappush(cards, res)

print(answer)