# 1208. Flatten

for t in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))

    for i in range(n):
        M = boxes.index(max(boxes))
        m = boxes.index(min(boxes))

        # 최댓값과 최솟값의 인덱스가 같을 경우 최솟값의 인덱스를 바꿔준다.
        if M == m:
            m = boxes[m+1:].index(min(boxes))
        
        boxes[M] -= 1
        boxes[m] += 1

    answer = max(boxes) - min(boxes)
    print(f'#{t} {answer}')