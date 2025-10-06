import sys; sys.stdin = open('input.txt', 'r')

def seq(start, cnt, path):

    if cnt == M:
        print(*path)
        return

    # i를 시작점으로 받아 내림차순이 발생하지 않음
    for i in range(start, N + 1):
        seq(i, cnt+1, path+[i])

T = int(input())
for tc in range(1, T+1):
    # 자연수 N, 수열 M개
    N, M = map(int, input().split())

    seq(1, 0, []) # 시작점, 횟수, path