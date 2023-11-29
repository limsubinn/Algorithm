n = int(input(), 8) # 8진수로 입력받는다.
print(bin(n)[2:])

'''
시간 초과

def change_to_decimal(n):
    number = 0
    for i, num in list(enumerate(n[::-1])):
        number += int(num) * (8 ** i)
    return number

def change_to_binary(number):
    answer = ''
    while number > 0:
        answer = str(number % 2) + answer
        number //= 2
    return answer

def solution(n):
    if n == '0':
        return 0
    number = change_to_decimal(n)
    answer = change_to_binary(number)
    return answer

n = input()
print(solution(n))
'''