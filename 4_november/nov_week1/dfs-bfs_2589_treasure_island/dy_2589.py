'''
# 각 칸은 육지(L)나 바다(W)로 표시되어 있다
# 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간
# 보물은 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳
# 보물이 있을 모든 가능성, 육지 2개를 뽑는 조합(==> 육지 위치 리스트 필요)
# 최단 거리 구하는 함수 구현(BFS, 큐)
# 모든 조합을 bfs 시도, 최대값과 비교


from collections import deque


# 세로 n, 가로 m
n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]


# 육지 위치 리스트 만들기
l_lst = deque()
for lr in range(n):
   for lc in range(m):
       if lst[lr][lc] == 'L':
           l_lst.append((lr, lc))


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# 최단 거리를 구하는 bfs
def bfs(f_idx, s_idx):
   fr, fc = l_lst[f_idx][0], l_lst[f_idx][1]
   sr, sc = l_lst[s_idx][0], l_lst[s_idx][1]
   # 시작점 삽입, (r, c, 걸리는시간)
   q = deque([(fr, fc, 0)])
   visited = [[True] * m for _ in range(n)]
   visited[fr][fc] = False
   while q:
       r, c, h = q.popleft()
       for i in range(4):
           nr = r + delta[i][0]
           nc = c + delta[i][1]
           if 0 <=nr<n and 0 <=nc<m:
               if lst[nr][nc] == 'L' and visited[nr][nc]:
                   # 도착지에 도착하면 함수 종료, 최단 시간 반환
                   if nr == sr and nc == sc:
                       return h+1
                   q.append((nr, nc, h+1))
                   visited[nr][nc] = False
   # 목적지에 도착하지 못했을 경우
   return -1


max_h = -1
l_num = len(l_lst)
path = [0]*2
# 보물이 있을 모든 가능성, 육지 2개 조합
# 모든 가능성을 bfs 시도
def recur(cnt, prev):
   global max_h


   if cnt == 2:
       hour = bfs(path[0], path[1])
       max_h = max(max_h, hour)
       return


   for i in range(prev, l_num):
       path[cnt] = i
       recur(cnt + 1, i)


recur(0, 0)
print(max_h)
'''

from collections import deque


# 세로 n, 가로 m
n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

# 육지 위치 리스트 만들기
l_lst = deque()
for lr in range(n):
   for lc in range(m):
       if lst[lr][lc] == 'L':
           l_lst.append((lr, lc))


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# bfs
def bfs(fr, fc):
   # 시작점 삽입, (r, c, 걸리는시간)
   q = deque([(fr, fc, 0)])
   visited = [[True] * m for _ in range(n)]
   visited[fr][fc] = False
   while q:
       r, c, h = q.popleft()
       for i in range(4):
           nr = r + delta[i][0]
           nc = c + delta[i][1]
           if 0 <=nr<n and 0 <=nc<m:
               if lst[nr][nc] == 'L' and visited[nr][nc]:
                   q.append((nr, nc, h+1))
                   visited[nr][nc] = False
   return h # 가장 오랜 걸린 시간 반환

max_h = -1

for r, c in l_lst:
    hour = bfs(r, c)
    max_h = max(max_h, hour)

print(max_h)

