# 프로그래머스 43163: 단어 변환

from collections import deque

def compare(a, b): # 알파벳이 하나만 다른지 판별
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    if cnt == 1:
        return True  
    return False


def bfs(i, words, visited, target):
    queue = deque()
    queue.append([words[i], 1]) # 단어, 변환 횟수 저장
    visited[i] = True
    
    while queue:
        word, result = queue.popleft()
        
        if word == target:
            return result

        for i in range(len(words)):
            if not compare(words[i], word):
                continue
            if visited[i]:
                continue
            
            visited[i] = True
            queue.append([words[i], result+1])
    
def solution(begin, target, words):
    if target not in words: # 변환할 수 없는 경우
        return 0
    
    visited = [False] * len(words)
    
    answer = 51
    for i in range(len(words)):
        if compare(words[i], begin):
            answer = min(answer, bfs(i, words, visited, target))

    return answer