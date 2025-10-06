'''
from collections import deque


#적록색약일때 세는 구역
#빨강 = 초록, 파랑
def yes():
   #방문 예정 리스트, 스택
   while y_stack:
       pass
   pass
#상하좌우에 같은 색이 있다면 구역




#아닐때 세는 구역
def no():
   pass


n = int(input())
lst = [list(input()) for _ in range(n)]
y_stack = deque()
n_stack = deque()


y_num = yes()
n_num = no()


print(n_num, y_num)
'''
from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# 적록색약일때 세는 구역
# 빨강 = 초록, 파랑
def yes(cnt):
    for r in range(n):
        for c in range(n):
            # 방문 한적 없는 곳이라면 num += 1
            if not y_v[r][c]:
                cnt += 1
                # 구역의 색 저장
                color = lst[r][c]
                if color == 'R' or color == 'G':
                    color = ['R', 'G']
                else:
                    color = ['B']
                # 방문 예정 목록
                stack = deque([(r, c)])
                # 방문 표시
                y_v[r][c] = True
                while stack:
                    # current, 현재 위치
                    c_r, c_c = stack.pop()
                    for i in range(4):
                        nr = c_r + dr[i]
                        nc = c_c + dc[i]
                        # 범위 안이고 color에 해당 색이 있다면
                        if 0 <= nr < n and 0 <= nc < n and lst[nr][nc] in color:
                            #방문한 적 없다면
                            if not y_v[nr][nc]:
                                stack.append((nr, nc))
                                y_v[nr][nc] = True
            # 상하좌우에 같은 색이 없을때까지 방문
    # 전체 순회를 끝났다면 cnt 반환
    return cnt


# 아닐때 세는 구역
def no(cnt):
    for r in range(n):
        for c in range(n):
            # 방문 한적 없는 곳이라면 num += 1
            if not n_v[r][c]:
                cnt += 1
                # 구역의 색 저장
                color = lst[r][c]
                # 방문 예정 목록
                stack = deque([(r, c)])
                # 방문 표시
                n_v[r][c] = True
                while stack:
                    # current, 현재 위치
                    c_r, c_c = stack.pop()
                    for i in range(4):
                        nr = c_r + dr[i]
                        nc = c_c + dc[i]
                        # 범위 안이고 색이 같다면
                        if 0 <= nr < n and 0 <= nc < n and lst[nr][nc] == color:
                            if not n_v[nr][nc]:
                                stack.append((nr, nc))
                                n_v[nr][nc] = True
    return cnt


n = int(input())
lst = [list(input()) for _ in range(n)]
# y방문 리스트
y_v = [[False]*n for _ in range(n)]
# n방문 리스트
n_v = [[False]*n for _ in range(n)]

y_num = yes(0)
n_num = no(0)

print(n_num, y_num)