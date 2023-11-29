from itertools import product

n, k = map(int, input().split())
array = list(input().split())

# 내림차순 정렬 -> 큰 수부터 뽑게 된다.
array.sort(reverse=True)
# n의 자릿수
digit = len(str(n))

while True:
    nums = list(product(array, repeat = digit))
    for i in nums:
        answer = int(''.join(i))
        if n >= answer:
            print(answer)
            exit()
    digit -= 1