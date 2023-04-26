string = input()

array = list(enumerate(string)) # 인덱스와 함께 저장
array.sort(key=lambda x:x[1]) # 사전 순 정렬

result = [''] * len(string)
stack = [] # 추가 기준이 될 인덱스 저장
size = 0 # 정답 길이

while True:
    for i, a in array:
        # 이미 정답에 있으면 넘어간다.
        if result[i]:
            continue
        # 현재 인덱스가 기준이 될 인덱스보다 작으면 넘어간다.
        if stack and stack[-1] >= i:
            continue
        result[i] = a
        print(''.join(result))
        stack.append(i)
        size += 1

    if size >= len(string):
        break

    # 인덱스 하나 빼기
    stack.pop()