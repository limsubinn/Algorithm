# 프로그래머스 17686: 파일명 정렬 (2018 KAKAO BLIND RECRUITMENT)

import re

def solution(files):
    answer = []
    array = [['', '', ''] for i in range(len(files))]
    
    for i in range(len(files)):
        # HEAD 저장
        tmp = re.split('[0-9]+', files[i])
        array[i][0] += tmp[0].lower()

        # 입력된 순서
        array[i].append(i)

        for j in range(len(tmp[0]), len(files[i])):
            # TAIL 저장
            if not files[i][j].isdigit():
                array[i][2] += files[i][j:]
                break
            # NUMBER 저장
            array[i][1] += files[i][j]
        array[i][1] = int(array[i][1])
    
    # 정렬 후 정답 배열에 추가
    array.sort(key=lambda x:(x[0], int(x[1]), x[3]))
    for i in array:
        answer.append(files[i[3]])

    return answer
