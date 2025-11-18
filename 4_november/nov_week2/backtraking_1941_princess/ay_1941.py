import sys
sys.stdin = open("1941_input.txt", "r")

# 0, 0 부터 확인하는데 그다음 부터는 0,0은 포함 시키지 않고 확인한다.
seats = [input() for _ in range(5)]
grid = [[0]*5 for _ in range(5)]
dirs = [(-1, 0), (0, 1), (-1, 0), (0, -1)] # 상, 우, 하, 좌
visited = [[0]*5 for _ in range(5)]
ans = 0

def rec(cnt, r, c, s_cnt): # 현재 구성 인원, 좌표값, 이다솜파 구성 인원수, cnt 시작은
    global ans
    if cnt == 7: # base_case
        if grid[r][c] == 1: # 마지막이 이미 체크한 위치면 개수 세지 않음
            return
        if s_cnt >= 4: # 이다솜파가 4명 이상일때만 개수 세도록
            ans += 1
        return
    for dr, dc in dirs: # dfs 구현
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >=5 or nc < 0 or nc >=5 or visited[nr][nc]:
            continue

        visited[nr][nc] = 1
        if seats[nr][nc] == 'S':
            s_cnt += 1

        rec(cnt+1, nr, nc, s_cnt)

        visited[nr][nc] = 0
        if seats[nr][nc] == 'S':
            s_cnt -= 1

# 시작점 잡기
for r in range(5):
    for c in range(5):
        s_cnt = 0
        grid[r][c] = 1
        visited[r][c] = 1
        if seats[r][c] == 'S':
            s_cnt += 1

        rec(1, r, c, s_cnt)

        visited[r][c] = 0
        if seats[r][c] == 'S':
            s_cnt -= 1
        visited[r][c] = 1

print(ans)