board = input()
size = 0
answer = ''

for b in board:
    if b != '.':
        size += 1
    else:
        if size % 2 != 0:
            answer = -1
            break
        while size >= 4:
            size -= 4
            answer += 'AAAA'
        if size > 0:
            answer += 'BB'
            size = 0
        answer += '.'

if answer != -1 and size > 0:
    if size % 2 != 0:
        size = 0
        answer = -1
    while size >= 4:
        size -= 4
        answer += 'AAAA'
    if size > 0:
        answer += 'BB'

print(answer)