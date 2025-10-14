def recur(cnt, start):
    # 기저조건
    if cnt == M:
        print(*path)
        return

    prev = -1  # 이전에 선택한 수를 기록 (중복 수열 방지)

    # 재귀 파트
    for i in range(start, N):
        if arr[i] == prev: continue
        path.append(arr[i])
        recur(cnt + 1, i + 1)
        path.pop()

        prev = arr[i]  # 현재 사용한 수를 기록

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path = []
recur(0, 0)