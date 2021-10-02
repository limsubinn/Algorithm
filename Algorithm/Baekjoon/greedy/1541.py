s = input().split('-')
res = 0

for i in range(len(s)):
    for j in s[i].split('+'):
        if i == 0:
            res += int(j)
        else:
            res -= int(j)

print(res)