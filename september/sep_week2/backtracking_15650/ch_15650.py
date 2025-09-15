# 재귀 완탐
# 문자열에 + 해서 직전 숫자와 비교 -> 직후 숫자가 더 작을 경우 리턴
N, M = map(int, input().split())

def recur(depth, path):
    if len(path) >= 2:
        if path[-2] > path[-1]: # 오름차순이 아니면 리턴
            return

    if depth == M:  # 기저조건: M개의 숫자를 모두 골랐을 때
        print(*path)
        return

    for i in range(1, N+1):
        if str(i) in path:   # 중복 건너뛰기
            continue
        recur(depth + 1, path + str(i))  # 문자열 path에 숫자들을 담아 비교

recur(0, '')