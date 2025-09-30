import sys; sys.stdin = open('input.txt', 'r')

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상

def dirty_more(sr, sc):
    num = dirty[sr][sc] // 5


def air_purifier():
    pass

T = int(input())
for tc in range(1, T+1):
    R, C, time = map(int, input().split()) # 가로R 세로C 작동 time초
    dirty = [list(map(int, input().split())) for _ in range(R)]
    spread = [[0]*C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if dirty[x][y] > 0:
                dirty_more(x, y)