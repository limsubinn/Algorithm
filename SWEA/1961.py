# 1961. 숫자 배열 회전

def rotate(original):
    return list(zip(*original[::-1]))

def to_string(row):
    return ''.join(row)

T = int(input())

for t in range(1, T+1):
    n = int(input())
    array = [list(input().split()) for _ in range(n)]

    rotate90 = rotate(array)
    rotate180 = rotate(rotate90)
    rotate270 = rotate(rotate180)

    print(f'#{t}')
    for i in range(n):
        print(to_string(rotate90[i]), to_string(rotate180[i]), to_string(rotate270[i]))