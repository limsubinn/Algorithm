# 프로그래머스 42577: 전화버호 목록

def solution(phone_book):
    phone_book.sort()
    
    for i in range(1, len(phone_book)):
        size = len(phone_book[i-1])
        if phone_book[i-1] == phone_book[i][:size]:
            return False
        
    return True