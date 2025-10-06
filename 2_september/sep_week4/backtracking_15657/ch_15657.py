# N개의 서로 다른 수 중 M개를 골라 출력
# 중복해서 골라도 되고 비내림차순이어야 함
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def recur(depth, path):
    if len(path) >= 2:  # 2개 이상 뽑혔을때부터 비내림차순인지 비교
        i = 0
        while i <= len(path) - 2:
            if path[i] > path[i + 1]:
                return
            i += 1
    if depth == M:  # 기저조건: M개의 수를 골랐을 때 출력
        print(*path)
        return
    for num in range(N):
        recur(depth + 1, path + [arr[num]])

recur(0, [])