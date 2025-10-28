import sys
sys.stdin = open("2468_input.txt", "r")
from collections import deque
drs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(r, c): # 안잠긴 영역 찾아서 표시
    q = deque([(r, c)])
    check_arr[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in drs:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= N or nc < 0 or nc >=N or check_arr[nr][nc] == 0:
                continue
            q.append((nr, nc))
            check_arr[nr][nc] = 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hights = set()

    for r in arr: # 높이 숫자 분포 구하기
        hights |= set(r)

    ans = 0
    hights = [0] + sorted(hights) # 비가 안오는 경우는 cnt = 1이 나와야 함 그런데 0을 안넣으면 0이 되어서 문제가 됨

    for h in hights: # 높이 별로 직접 물에 잠기는지 확인 높이 순차적으로 높이면서 잠기는 부분 0으로 바꿔줌
        # 잠기는 영역 0으로 변환
        for r in range(N):
            for c in range(N):
                if arr[r][c] == h: # 해당 높이랑 같은 높이만 0으로 바꾸면됨 이전 높이는 이미 바꿨으니까
                    arr[r][c] = 0

        check_arr = [row[:] for row in arr] # 원본 안헤치고 복사
        now_cnt = 0
        # 안잠긴 영역 찾기
        for r in range(N):
            for c in range(N):
                if check_arr[r][c]:
                    bfs(r, c)
                    now_cnt += 1
        if now_cnt > ans:
            ans = now_cnt
    # if ans == 0:
    #     ans = 1
    print(ans)


