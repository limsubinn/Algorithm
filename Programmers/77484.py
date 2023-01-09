# 프로그래머스 77484: 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    worst = 7    
    for i in lottos:
        if i in win_nums:
            worst -= 1
    
    best = worst - lottos.count(0)
    
    if best == 7:
        best = 6
    if worst == 7:
        worst = 6
    
    return [best, worst]