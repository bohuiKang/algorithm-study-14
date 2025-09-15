import sys; sys.stdin = open('input.txt','r')

def check(num, cnt):

    if cnt == M:
        print(*path)
        return

    for i in range(1, N+1): # N=3, 1 2 3
        path.append(i)
        check(i, cnt + 1)
        path.pop()

T = int(input())
for tc in range(1, T+1):
    # 자연수 N, 수열 M
    N, M = map(int, input().split())
    path = []

    check(0, 0) # 시작 수, 수열 길이 체크