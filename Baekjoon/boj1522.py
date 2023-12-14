# 백준 1522: 문자열 교환

s = list(input())

# 'a'의 개수 세기
cnt = 0
for i in s:
    if i == 'a':
        cnt += 1

# 원형
s += s[:cnt]

# 슬라이딩 윈도우 -> 옮기면서 'b'의 개수 세기
temp = 0
for i in range(cnt):
    if s[i] == 'b':
        temp += 1
answer = temp

for i in range(cnt, len(s)):
    if s[i-cnt] == 'b':
        temp -= 1
    if s[i] == 'b':
        temp += 1
    answer = min(answer, temp)

print(answer)