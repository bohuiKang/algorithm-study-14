import sys
sys.stdin = open("1697_input.txt", "r")
from collections import deque
# sys.setrecursionlimit(10**6)
N, K = map(int, input().split()) # 수빈, 동생
MAX = 100000
# 순간이동은 오른쪽으로만
# 동생이 왼쪽에 있으면 N > K 시간 N-K
# 동생이 오른쪽에 있으면 (N < K)
# 2 * N 을 하거나 , x-1 , x+1 하기


# dfs로는 절대 안풀려요

if N >= K:
    print(N-K)
else:
    dist = [-1] * (MAX+1)
    q = deque([N])
    dist[N] = 0
    while q:
        n = q.popleft()
        if n == K:
            print(dist[n])
            break
        for next_n in (n-1, n+1, n*2):
            if next_n < 0 or next_n > MAX or dist[next_n] > -1 :
                continue
            dist[next_n] = dist[n] + 1
            q.append(next_n)


#
# best = [float('inf')]*100001 # 각 위치에 도달한 최소 시간 기록
# min_time = float('inf')
# def rec(N, time): # 초기 N < K인 경우 최단 시간 찾는 함수
#     global min_time, abs_NK
#
#     if N < 0 or N > 100000: # 범위 초과시 종료
#         return
#
#     if N == K: # K 일치시 값 비교
#         min_time = time # min 안쓰는 이유 이전에 이미 큰 값이면 아래 조건에서 짤림
#         return
#
#     if time == min_time: # 현재까지 시간이 min_time과 같으면 더이상 탐색할 필요 없음
#         return
#
#     if time >= best[N]: # 이 위치 더 빨리 온적 있으면 컷
#         return
#
#     if time >= abs_NK: # 초기 둘사이 값보다 크면 더이상 탐색할 필요 없음
#         return
#
#
#
#     best[N] = time
#
#     rec(2 * N, time + 1) # dfs 구현
#     rec(N - 1, time + 1)
#     rec(N + 1, time + 1)
#
#
# def check_time(N, K): # 최종 시간 체크 하는 함수
#     global min_time, abs_NK
#     abs_NK = abs(N-K)
#     min_time = abs_NK
#
#     if N >= K:
#         min_time = abs_NK
#         return
#     if N < K:
#         rec(N, 0)
#
# check_time(N, K)
# print(min_time)
#




