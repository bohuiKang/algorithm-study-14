# 비내림차순: 항상 왼쪽요소 <= 오른쪽요소 여야 하는 수열
N, M = map(int, input().split())
def recur(depth, path):
    for i in range(depth - 1):  # 내림차순이 되면 바로 종료
        if path[i] > path[i + 1]:
            return
    if depth == M:  # 기저조건: M개의 수를 모두 고르면 종료
        print(*path)
        return
    for i in range(1, N + 1):   # 1~N의 수들 중 한개를 추가해서 다음 재귀로 넘겨줌
        recur(depth + 1, path + [i])
recur(0, [])