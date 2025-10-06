import sys; sys.stdin = open('input.txt', 'r')

def seq(cnt, path):
    global visited
    if cnt == M:
        print(*path)
        return

    # i를 시작점으로 받아 내림차순이 발생하지 않음
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            seq(cnt+1, path+[arr[i]])
            visited[i] = False

T = int(input())
for tc in range(1, T+1):
    # N개의 수, 수열 M개
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    visited = [False] * N
    seq(0, []) # 횟수, path