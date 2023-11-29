# 프로그래머스 84512: 모음사전

def solution(word):
    alphabet = {'A':'E', 'E':'I', 'I':'O', 'O':'U', 'U':''}
    result = ''
    answer = 0

    while result != word:
        # 길이가 5보다 작으면 'A' 추가
        if len(result) < 5:
            result += 'A'
        # 길이가 5이면 다음 단어로 교체
        else:
            for i in range(4, -1, -1):
                r = result[i]
                result = result[:i] + alphabet[r] + result[i+1:]
                if r != 'U':
                    break
        answer += 1
  
    return answer