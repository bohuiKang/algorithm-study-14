from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 세로 n, 가로 m
n, m = map(int, input().split())

# 연구소
# 0은 빈칸, 1은 벽, 2는 바이러스
lst = [list(map(int, input().split())) for _ in range(n)]
# 빈칸 위치 리스트
z_lst = deque()
# 바이러스 위치 리스트
v_lst = deque()


# 바이러스, 빈칸 위치 찾는 함수
def find():
    for r in range(n):
        for c in range(m):
            if lst[r][c] == 0:
                z_lst.append((r, c))
            elif lst[r][c] == 2:
                v_lst.append((r, c))


find()

# 빈칸의 개수
z_num = len(z_lst)
# 바이러스의 수
v_num = len(v_lst)


# 바이러스 전염 함수, 안전 영역의 개수(빈칸의 수 - 새로 전염시킨 바이러스 전염의 수) 반환
def virus(lab):
    # 바이러스 위치 복사
    q = v_lst.copy()
    # 바이러스 전염의 수
    v = 0
    while q:
        r, c = q.pop()
        # 바이러스의 수 증가
        v += 1
        # 상하좌우 탐색
        for i in range(4):
            nr, nc = r + delta[i][0], c + delta[i][1]
            # 감염시킬 수 있다면
            if 0 <= nr < n and 0 <= nc < m and lab[nr][nc] == 0:
                lab[nr][nc] = 2
                q.append((nr, nc))
    # 안전 영역의 수 반환 (초기 빈칸의 수 - 새로 세운 벽의 수) - (바이러스 수 - 기존에 있던 바이러스 수)
    return (z_num - 3) - (v - v_num)


# 벽을 세울 수 있는 조합 확인
path = [0] * 3
max_s = 0


def recur(cnt, prev):
    global max_s

    if cnt == 3:
        # 지도 복사
        lab = [l[:] for l in lst]
        for p in path:
            r, c = z_lst[p]
            # 벽 세우기
            lab[r][c] = 1
        # 벽을 세운 지도로 안전 영역 수 세기
        s_num = virus(lab)
        max_s = max(max_s, s_num)
        return

    for i in range(prev, z_num):
        path[cnt] = i
        recur(cnt+1, i+1)

recur(0, 0)
print(max_s)
