def recur(cnt):
    # 기저조건
    if cnt == M:
        key = tuple(path)
        if key not in ans_list:
            ans_list.add(key)
            print(*path)  # 기존에 없던거면 넣고 프린트하기
        return

    # 재귀 파트
    for i in range(N):
        if not visited[i]:  # 중복 뽑는거 제거
            path.append(arr[i])
            visited[i] = 1
            recur(cnt + 1)
            path.pop()
            visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans_list = set()

path = []
visited = [0] * N
recur(0)