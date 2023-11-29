def find_answer(crane, box):
    crane.sort(reverse = True)
    box.sort(reverse = True)

    if crane[0] < box[0]:
        return -1
    
    answer = 0

    while box:
        for c in crane:
            if box and c < box[-1]:
                continue
            for b in box:
                if b <= c:
                    box.remove(b)
                    break
        answer += 1
    
    return answer

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

print(find_answer(crane, box))