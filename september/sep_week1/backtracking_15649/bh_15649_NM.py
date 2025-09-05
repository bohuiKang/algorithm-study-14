# N과 M (1)
import sys; sys.stdin = open('15649_input.txt', 'r')

def recur(cnt):
    global path
    global visited

    if cnt == M:
        print(*path)
        return

    for i in range(1, N+1):
        if visited[i]:
            continue
        path.append(i)
        visited[i] = 1
        recur(cnt+1)
        path.pop()
        visited[i] = 0


# 중복 없는 수열
T = int(input())
for tc in range(1, T+1):
    # 1~N까지 중복없이 M개를 고른 수열
    N, M = map(int, input().split())
    path = []
    visited = [0] * (N+1)
    recur(0)

