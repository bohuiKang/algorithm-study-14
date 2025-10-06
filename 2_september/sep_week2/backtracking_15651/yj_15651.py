N, M = map(int, input().split())  # 1~N 중에서 M개를 골라야 한다. 중복 가능

def recur(cnt):
    if cnt == M:  # 기저조건: M개 다 고르면 stop
        print(*path)
        return

    # 재귀 파트
    for i in range(1, N + 1):
        path.append(i)
        recur(cnt + 1)
        path.pop()

path = []
recur(0)