# 프로그래머스 12971: 스티커 모으기(2)

def solution(sticker):
    size = len(sticker)

    # 스티커의 길이가 2 이하이면 스티커의 최댓값 == 정답
    if size <= 2:
        return max(sticker)

    answer = 0

    # 첫 번째 스티커를 선택한 경우
    dp = [[0] * 2 for _ in range(size - 1)]
    dp[0][1] = sticker[0]
    for i in range(1, size - 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + sticker[i]
    answer = max(answer, max(dp[-1]))

    # 첫 번째 스티커를 선택하지 않은 경우
    dp = [[0] * 2 for _ in range(size)]
    for i in range(1, size):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + sticker[i]
    answer = max(answer, max(dp[-1]))

    return answer