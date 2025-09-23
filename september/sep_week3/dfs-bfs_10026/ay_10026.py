import sys
sys.stdin = open("input.txt", "r")

from collections import deque

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] #우하좌상
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    picture = [input() for _ in range(N)]

    def bfs(r, c):
        q = deque([(r, c)])

        while q:
            nr, nc = q.popleft()





