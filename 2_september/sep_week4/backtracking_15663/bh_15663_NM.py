import sys; sys.stdin = open('input.txt', 'r')

# used 사용
def seq(cnt, path):
    if cnt == M:
        print(*path)
        return

    used = -1 # 현재 깊이에서 이미 쓴 숫자를 기록하는 역할
    for i in range(N):
        if not visited[i] and arr[i] != used:
            visited[i] = 1
            seq(cnt+1, path+[arr[i]])
            visited[i] = 0
            used = arr[i]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 자연수 N, 수열 M개
    arr = sorted(list(map(int, input().split())))
    visited = [0] * N

    seq(0, []) # 횟수, path

## set, tuple 사용
# def seq(cnt, path):
#     if cnt == M:
#         if tuple(path) not in paths:
#             paths.add(tuple(path))
#             print(*path)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = 1
#             seq(cnt + 1, path + [arr[i]])
#             visited[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())  # 자연수 N, 수열 M개
#     arr = sorted(list(map(int, input().split())))
#     visited = [0] * N
#     paths = set()
#     seq(0, [])  # 횟수, path