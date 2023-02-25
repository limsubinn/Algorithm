# 프로그래머스 12909: 올바른 괄호

def solution(s):    
    stack = []
    
    for i in s:
        if stack and i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)
            
    if stack:
        return False
    
    return True

'''
정확성 테스트(O) 효율성 테스트(X)

def solution(s):    
    while "()" in s:
        s = s.replace("()", "")
    
    if s:
        return False

    return True
'''
