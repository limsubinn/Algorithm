n = int(input())
cnt = 0

for i in range(n):
    word = list(input())
    word2 = [word[0]]
    flag = 0

    for i in word:
        if i!=word2[len(word2)-1]:
            if i in word2:
                flag = 1
            else:
                word2.append(i)

    if flag==0 :
        cnt += 1

print(cnt)