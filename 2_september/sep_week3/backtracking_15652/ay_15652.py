import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    path = []
    def backtracking(idx, cnt):
        if cnt == M:
            print(*path)
            return

        for i in range(idx, N+1):
            path.append(i)
            backtracking(i, cnt+1)
            path.pop()

    backtracking(1, 0)