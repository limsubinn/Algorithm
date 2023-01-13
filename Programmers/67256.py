# 프로그래머스 67256: 키패드 누르기 (2020 카카오 인턴십)

def solution(numbers, hand):
    answer = ''
    keypad = {1: [0,0], 2: [0,1], 3: [0,2],
             4: [1,0], 5: [1,1], 6: [1,2],
             7: [2,0], 8: [2,1], 9: [2,2],
             '*': [3,0], 0: [3,1], '#': [3,2]}

    l = '*'
    r = '#'
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            l = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            r = i
        else:
            lenL = abs((keypad[i][0] - keypad[l][0])) + abs((keypad[i][1] - keypad[l][1]))
            lenR = abs((keypad[i][0] - keypad[r][0])) + abs((keypad[i][1] - keypad[r][1]))
            if lenL > lenR:
                answer += 'R'
                r = i
            elif lenL < lenR:
                answer += 'L'
                l = i
            else:
                if hand == 'right':
                    answer += 'R'
                    r = i
                else:
                    answer += 'L'
                    l = i
                 
    return answer