# 프로그래머스 17680: 캐시 (2018 KAKAO BLIND RECRUITMENT)

def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0: # 캐시 크기 0일 때 처리
        return 5 * len(cities)

    cache = [""] * cacheSize
    time = [i for i in range(cacheSize)]
    i = cacheSize

    for city in cities:
        city = city.lower() # 소문자 변환

        if city in cache: # cache hit
            answer += 1
            idx = cache.index(city)
        else: # cache miss
            answer += 5
            idx = time.index(min(time)) # 참조 시간이 가장 오래된 인덱스
            cache[idx] = city

        time[idx] = i # 캐시 참조 시간 기록
        i += 1
    
    return answer