def can_attach(c, r, size):
    if c + size > 10 or r + size > 10:
        return False

    # 범위를 만족하는 색종이인지 확인 -> size를 넘어가면 만족하지 못함
    for i in range(c, c + size):
        for j in range(r, r + size):
            if arr[i][j] != 1:
                return False

    return True

def attach(c, r, size, attached):
    for i in range(c, c+size):
        for j in range(r, r+size):
            # attached = 0 -> 색종이 붙인 것, attached = 1 -> 색종이 떼어냄 (본래 상태로 복귀)
            arr[i][j] = attached

def dfs(c, r, cnt):
    global result

    # 가지치기
    if cnt >= result:
        return

    # arr 다 돎 -> 결과 갱신
    if c >= 10:
        result = min(result, cnt)
        return

    # 다음 줄로 넘어가기
    if r >= 10:
        dfs(c + 1, 0, cnt)
        return

    # 0이면 그냥 지나가감
    if arr[c][r] == 0:
        dfs(c, r + 1, cnt)
        return

    for size in range(5, 0, -1):
        if paper[size] and can_attach(c, r, size):
            attach(c, r, size, 0)
            paper[size] -= 1
            dfs(c, r + size, cnt + 1)
            attach(c, r, size, 1)
            paper[size] += 1

paper = [0, 5, 5, 5, 5, 5]

arr = [list(map(int, input().split())) for _ in range(10)]
result = float('inf')

dfs(0, 0, 0)

print(-1 if result == float('inf') else result)