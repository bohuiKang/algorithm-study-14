# 이걸 한다고 확연하게 빨라지지는 않아 그냥 뺌
# import sys
# input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solve():
    r, c, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(r)]

    # 공기청정기 위치 찾기
    fresher = []
    for i in range(r):
        if arr[i][0] == -1:
            fresher.append((i, 0))

    def diffusion():
        scores = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if arr[i][j] > 0:
                    # 분배되는 양
                    spread_amount = arr[i][j] // 5
                    spread_cnt = 0
                    for k in range(4):
                        ni, nj = i + dr[k], j + dc[k]
                        # 유효성 검증 (범위 안에 있고 공기 청정기가 아니라면)
                        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                            scores[ni][nj] += spread_amount
                            spread_cnt += 1
                    # 원래 양에서 뼈져나간만큼 ....
                    scores[i][j] += arr[i][j] - spread_amount * spread_cnt
        # 공기청정기 위치
        for fy, fx in fresher:
            scores[fy][fx] = -1
        return scores

    # 공기청정기 작동
    def fresh():
        top, _ = fresher[0]
        bottom, _ = fresher[1]

        # 위쪽
        for i in range(top-1, 0, -1):
            arr[i][0] = arr[i-1][0]
        for j in range(c-1):
            arr[0][j] = arr[0][j+1]
        for i in range(top):
            arr[i][c-1] = arr[i+1][c-1]
        for j in range(c-1, 1, -1):
            arr[top][j] = arr[top][j-1]
        arr[top][1] = 0

        # 아래쪽
        for i in range(bottom+1, r-1):
            arr[i][0] = arr[i+1][0]
        for j in range(c-1):
            arr[r-1][j] = arr[r-1][j+1]
        for i in range(r-1, bottom, -1):
            arr[i][c-1] = arr[i-1][c-1]
        for j in range(c-1, 1, -1):
            arr[bottom][j] = arr[bottom][j-1]
        arr[bottom][1] = 0

    # T초 동안 돌아감
    for _ in range(t):
        #매 초마다 arr의 미세먼지 확산
        arr = diffusion()
        #공기청정기 가동
        fresh()

    # 미세먼지 다 합해서 출력
    total = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                total += arr[i][j]
    print(total)

# 실행
solve()
