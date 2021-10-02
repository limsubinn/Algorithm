import sys
n = int(sys.stdin.readline())
word = []

for i in range(n):
    word.append(sys.stdin.readline().rstrip())

word = list(set(word))  # 중복 제거
word.sort()             # 알파벳 순서대로 정렬
word.sort(key = len)    # 길이 순서대로 정렬

for i in word:
    print(i)