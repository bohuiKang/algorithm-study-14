import sys; sys.stdin = open('input.txt','r')

N = int(input()) # map size
complex = [list(map(int, input())) for _ in range(N)] # apartment complex

# 상좌하우
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

address = 1
house = []

def check(sr, sc):
    global cnt

    for i in range(4): # 상하좌우를 확인
        nr = sr + dr[i]
        nc = sc + dc[i]

        if 0 <= nr < N and 0 <= nc < N: # 범위를 벗어나지 않고
            if complex[nr][nc] == 1: # 주변 값 1이면 address 로 변경 후 탐색
                cnt += 1
                complex[nr][nc] = address
                check(nr, nc)

for r in range(N):
    for c in range(N):

        if complex[r][c] == 1: # 확인 안한 아파트가 있으면,
            cnt = 1
            address += 1 # address += 1로 변경 후 complex 리스트 값 변경
            complex[r][c] = address
            check(r, c) # 행, 열
            house.append(cnt)

print(address-1)
house.sort()
for i in house:
    print(i)
