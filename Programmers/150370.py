# 프로그래머스 150370: 개인정보 수집 유효기간 (2023 KAKAO BLIND RECRUITMENT)

def solution(today, terms, privacies):
    answer = []
    
    terms_dic = {}
    for i in terms:
        terms_dic[i.split()[0]] = int(i.split()[1]) * 28
        
    todayDate = list(map(int, today.split('.')))
    td = todayDate[0] * 12 * 28 + todayDate[1] * 28 + todayDate[2]
    
    n = 1
    for i in privacies:
        date = list(map(int, i.split()[0].split('.')))
        d = date[0] * 12 * 28 + date[1] * 28 + date[2] + terms_dic[i.split()[1]] - 1
    
        if td > d:
            answer.append(n)
            
        n += 1
 
    return answer