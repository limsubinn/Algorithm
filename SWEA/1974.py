# 1974. 스도쿠 검증

def check_row(array):
    for i in range(9):
        if len(set(array[i])) != 9:
            return False
    return True
    
def check_miniboard():
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            temp = set()
            for i in range(3):
                for j in range(3):
                    temp.add(board[x+i][y+j])
            if len(temp) != 9:
                return False
    return True

t = int(input())

for test_case in range(1, t+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    temp = list(zip(*board)) # 전치행렬

    # 가로, 세로, 3x3 확인
    if check_row(board) and check_row(temp) and check_miniboard():
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')