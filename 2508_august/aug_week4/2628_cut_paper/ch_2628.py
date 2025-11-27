'''
1. 종이 크기를 2배로 늘려서 2차원 배열을 만든다.
2. 가장자리를 포함해서 종이가 잘리는 모서리는 1, 안잘린 면은 0으로 한다.
3. 행우선, 열우선 순회를해서 잘린 종이들마다 행과 열에 0의 개수 +1이 각각 가로와 세로다. 
    (가로 x 세로 = 넓이)
4. 마지막에 넓이에서 나누기 4를 해주면 답이다.
'''

M, N = map(int, input().split())    # M: 가로(열), N: 세로(행)
M *= 2; N *=2
arr = [[0]* (M + 1) for _ in range(N + 1)]  # 모서리를 포함하여 생성
# 가장자리 1로 설정
for i in range(N + 1):
    arr[i][0] = arr[i][M] = 1
for j in range(M + 1):
    arr[0][j] = arr[N][j] = 1
T = int(input())
# 종이 자르기
for _ in range(T):
    direction, cut = map(int, input().split())  # direction: 0 가로, 1 세로 / cut: 자르는 위치
    cut *= 2
    if direction == 0:
        for j in range(M):
            arr[cut][j] = 1
    else:
        for i in range(N):
            arr[i][cut] = 1
# 자른 종이 넓이 비교
Dx = [-1, 1]
max_v = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt_x = cnt_y = 2   # i,j 중앙좌표 1과 넓이에 쓸 +1을 합해서 2부터 시작
            for p in range(2): 
                Ni, Nj = i, j + Dx[p]
                while arr[Ni][Nj] != 1:
                    cnt_x += 1
                    Nj += Dx[p]
            for p in range(2):
                Ni, Nj = i + Dx[p], j
                while arr[Ni][Nj] != 1:
                    cnt_y += 1
                    Ni += Dx[p]
            max_v = max(max_v, cnt_x * cnt_y)
# 가로 세로를 두배 늘렸으므로 넓이는 나누기 4
print(max_v // 4)