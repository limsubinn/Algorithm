# 프로그래머스 82612: 부족한 금액 계산하기

def solution(price, money, count):
    need = 0

    for i in range(1, count+1):
        need += price * i
    
    if need > money:
        return need-money
    else:
        return 0