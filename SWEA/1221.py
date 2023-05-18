# 1221. GNS

def transfer(dic):
    for i, word in enumerate(words):
        words[i] = dic[word]

s2n = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
       'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
n2s = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR',
       5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

T = int(input())

for t in range(1, T+1):
    a, b = input().split()
    words = list(input().split())

    # 문자열 -> 숫자
    transfer(s2n)
    # 정렬
    words.sort()
    # 숫자 -> 문자열
    transfer(n2s)

    print(f'#{t}')
    for word in words:
        print(word, end=' ')
    print()