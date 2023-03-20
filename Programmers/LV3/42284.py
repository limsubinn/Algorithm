# 프로그래머스 42844: 단속카메라

def solution(routes):
    routes.sort(key=lambda x:(x[0], x[1]))

    i = 1
    answer = 1
    camera = routes[0] # 카메라를 설치할 범위  

    for i in range(len(routes)):
        # 카메라를 설치할 수 있는 범위 안에 경로가 존재할 때
        if camera[1] >= routes[i][0]:
            camera = [routes[i][0], min(camera[1], routes[i][1])]
        # 카메라를 설치할 수 있는 범위 안에 경로가 존재하지 않을 때
        else:
            camera = routes[i]
            answer += 1

    return answer