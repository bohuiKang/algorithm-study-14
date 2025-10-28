import sys
sys.stdin = open("2583_input.txt", "r")
sys.setrecursionlimit(10**6) # 재귀 초과라 한도 풀어주기
from collections import deque

def dfs(r, c): # 넓이 세는 코드
    global cnt
    arr[r][c] = 1 # 체크한 위치는 1로 바꿔줘서 중복 체크 안하도록
    for dr, dc in dirs:
        nr, nc = r+dr , c+dc
        if nr < 0 or nr >= M or nc <0 or nc >= N or arr[nr][nc] == 1: # 범위 밖이면 건너뜀
            continue
        cnt += 1
        dfs(nr, nc)

# def dfs_3(r, c): # 넓이 세는 코드, 전역 변수 불러오지 않고 쓰기
#     cnt = 1
#     arr[r][c] = 1 # 체크한 위치는 1로 바꿔줘서 중복 체크 안하도록
#     for dr, dc in dirs:
#         nr, nc = r+dr , c+dc
#         if nr < 0 or nr >= M or nc <0 or nc >= N or arr[nr][nc] == 1: # 범위 밖이면 건너뜀
#             continue
#         cnt += dfs_3(nr, nc)
#     return cnt
#
# def dfs_2(r, c): # 비재귀 dfs
#     cnt = 1
#     stack = deque([(r, c)])
#     arr[r][c] = 1
#     while stack:
#         r, c = stack.pop()
#         for dr, dc in dirs:
#             nr, nc = r + dr, c + dc
#             if nr < 0 or nr >= M or nc < 0 or nc >= N or arr[nr][nc] == 1:  # 범위 밖이면 건너뜀
#                 continue
#             arr[nr][nc] = 1
#             cnt += 1
#             stack.append((nr, nc))
#     return cnt

M, N, K = map(int, input().split()) # y축, x축, 좌표 개수
arr = [[0]*N for i in range(M)]
dirs = [(-1,0), (1,0), (0,-1), (0, 1)] # 상하좌우

# arr에 직사각형 칠하기
for k in range(K): # K개의 좌표 (왼쪽 아래 x,y 오른쪽 위 x,y)
    x1, y1, x2, y2 = map(int, input().split()) # 좌표값 입력
    for r in range(y1, y2):
        for c in range(x1, x2):
            if arr[r][c] == 1: # 이미 처리해준 값이면 값 대입 코드 건너뜀 - 직사각형 영역 겹치는 경우
                continue
            arr[r][c] = 1 # 직사각형 1로 바꾸기

areas = []
for r in range(M): # 직사각형 아닌 위치 + 아직 세지 않은 영역 찾기
    for c in range(N):
        cnt = 1
        if arr[r][c] == 1:
            continue
        dfs(r, c)
        areas += [cnt]
areas.sort()
print(len(areas))
print(*areas)


# # 비재귀 dfs_2용 코드
# areas = []
# for r in range(M): # 직사각형 아닌 위치 + 아직 세지 않은 영역 찾기
#     for c in range(N):
#         if arr[r][c] == 1:
#             continue
#         areas.append(dfs_2(r, c))
# areas.sort()
# print(len(areas))
# print(*areas)

# # 전역 변수 없이 쓰기 - 시간 더 걸림 - 함수간 문제 생긱는 경우는 방지
# areas = []
# for r in range(M): # 직사각형 아닌 위치 + 아직 세지 않은 영역 찾기
#     for c in range(N):
#         if arr[r][c] == 1:
#             continue
#         areas.append(dfs_3(r, c))
# areas.sort()
# print(len(areas))
# print(*areas)

