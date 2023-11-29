# 프로그래머스 42584: 주식가격

def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break
                
    return answer


'''
스택을 이용한 풀이

def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    s = [0]
    
    for i in range(1, len(prices)-1):
        while s and prices[s[-1]] > prices[i]:
            p = s.pop()
            answer[p] = i - p
        s.append(i)
        
    return answer
'''