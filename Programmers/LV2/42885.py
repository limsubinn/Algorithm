# 프로그래머스 42885: 구명보트

def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1
    
    while True:
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        answer += 1

        if i == j:
            return answer + 1
        
        if i > j:
            return answer