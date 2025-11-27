def dfs(player, temp):
    global result

    if player == 11:
        result = max(result, temp)
        return

    for pos in range(11):
        if not visited[pos] and positions[player][pos] != 0:
            visited[pos] = True
            dfs(player + 1, temp + positions[player][pos])
            visited[pos] = False

T = int(input())

for _ in range(T):
    positions = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    result = 0

    dfs(0, 0)
    print(result)