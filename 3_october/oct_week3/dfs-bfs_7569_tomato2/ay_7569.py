M, N, H = map(int, input().split())

tomatos = [list(map(int, input().split())) for _ in range(N)]

def check_tomato():
    ans = 0
    for r in range(N):
        for c in range(M):
            if tomatos == 1