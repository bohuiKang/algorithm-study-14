import sys; sys.stdin = open('input.txt', 'r')

def seq(start, cnt, path):

    if cnt == M:
        print(*path)
        return

    for i in range(start, N):
        seq(i, cnt+1, path+[arr[i]])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 자연수 N, 수열 M개
    arr = sorted(list(map(int, input().split())))

    seq(0, 0, []) # 시작점, 횟수, path