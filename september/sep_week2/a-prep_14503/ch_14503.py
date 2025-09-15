# 그냥 하라는대로 구현

# 1. 방의 상태를 2차원 배열로 받음
N, M = map(int, input().split())    # NxM 배열
r, c, d = map(int, input().split()) # r, c: 청소기 시작좌표 / d: 방향 [0: 북, 1: 동, 2: 남, 3: 서]
arr = [list(map(int, input().split())) for _ in range(N)]   # arr: 방의 상태를 나타내는 배열 [0: 방, 1: 벽]

# 2. 로봇 청소기 구현
def vacuum(Si, Sj, d, result):
    Dr, Dc = [-1, 0, 1, 0], [0, 1, 0, -1]   # 4방향 델타 (북, 동, 남, 서)
    # 해당 칸 청소
    if arr[Si][Sj] == 0:
        arr[Si][Sj] = 2
        result += 1
    # 주변 4칸 중 빈 칸을 탐색
    for p in range(4):
        Ni, Nj = Si + Dr[p], Sj + Dc[p]
        if arr[Ni][Nj] == 0:
            break
    # 빈 칸이 없는 경우
    else:
        back = (d + 2) % 4  # 후진 방향
        Pi, Pj = Si + Dr[back], Sj + Dc[back]
        if arr[Pi][Pj] == 1:
            return result
        return(vacuum(Pi, Pj, d, result))
    # 빈 칸이 있는 경우
    while True:
        d = (d + 3) % 4  # 반시계 방향 회전
        Ni, Nj = Si + Dr[d], Sj + Dc[d]
        if arr[Ni][Nj] == 0:
            return(vacuum(Ni, Nj, d, result))

print(vacuum(r, c, d, 0))