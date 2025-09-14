dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1] # 상하좌우

N =int(input())
apt_map = [input() for _ in range(N)] # 문자열로 받음
visited = [[0]*N for _ in range(N)]



def recur(r, c):

    visited[r][c] = 1
    cnt = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >=N or nc < 0 or nc >=N:
            continue
        if not visited[nr][nc] and apt_map[nr][nc] == "1":
            cnt += recur(nr, nc)

    return cnt




numbers = []
for r in range(N):
    for c in range(N):
        if not visited[r][c] and apt_map[r][c] == "1":
            numbers.append(recur(r, c))

numbers.sort()
print(len(numbers))

for i in range(len(numbers)):
    print(numbers[i])




