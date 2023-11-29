# 프로그래머스 1845: 폰켓몬

def solution(nums):
    n = len(nums)
    if len(set(nums)) > n // 2:
        return n // 2
    return len(set(nums))