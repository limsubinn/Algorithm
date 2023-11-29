def flag(n):
    n_list = list(str(n))

    if len(n_list) > 2 :
        d = int(n_list[1]) - int(n_list[0])
        m = int(n_list[1])

        for i in n_list[2:]:
            if int(i)-m != d :
                return 0
            else :
                m = i

    return 1

n = int(input())
cnt = 0

for i in range(n):
    if flag(i+1) == 1 :
        cnt += 1

print(cnt)