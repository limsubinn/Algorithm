from collections import defaultdict

name = list(input())
name.sort()

# 알파벳 : 나타난 횟수
dic = defaultdict(int)
for i in name:
    dic[i] += 1


result = '' # 대칭이 될 단어
temp = '' # 중심이 될 단어

for key in dic:
    # 단어 붙이기
    result += key * (dic[key] // 2)
    # 단어가 나온 횟수가 홀수이면 중심 만들어주기
    if dic[key] % 2 != 0:
        temp += key

# 단어가 나온 횟수가 홀수인 경우가 1을 초과할 경우 팰린드롬을 만들 수 없다.
if len(temp) > 1:
    print('I\'m Sorry Hansoo')
# 단어를 대칭해서 붙인다.
else:
    print(result + temp + result[::-1])