def transpose(array):
    return list(zip(*array))

def find(visited):
    # 배열 전치 (세로 확인)
    temp = [''.join(i) for i in transpose(result)]
    # 단어를 순회하면서
    for i in temp:
        for j in range(6):
            # 해당 단어가 존재하는 단어이고, 나타난 적이 없는 단어이면 체크
            if not visited[j] and i == words[j]:
                visited[j] = True
                break
    # 모든 단어가 사용되었으면 True 리턴
    if all(visited):
        return True
    # 모든 단어가 사용되지 않았으면 False 리턴
    return False

def sol():
    # 단어 3개 고르기
    for i in range(6):
        for j in range(6):
            for k in range(6):
                # 중복되는 단어가 있으면 continue
                if i == j or j == k or k == i:
                    continue

                visited = [False] * 6

                # 퍼즐 만들기
                result[0] = words[i]
                result[1] = words[j]
                result[2] = words[k]

                # 사용한 단어 체크
                visited[i] = True
                visited[j] = True
                visited[k] = True

                # 세로 단어 찾기
                if find(visited):
                    return result
    return 0


words = [input() for _ in range(6)]
result = [[''] * 3 for _ in range(3)]

answer = sol()
if answer == 0:
    print(0)
else:
    for i in result:
        print(''.join(i))
