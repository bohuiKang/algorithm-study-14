def check_power(cnt, power):
    global max_power

    if cnt == 11:
        max_power = max(max_power, power)
        return

    for position in range(11):
        if inform[cnt][position] == 0:
            continue
        if not visited[position]: # 포지션에 누가 없으면
            visited[position] = 1
            check_power(cnt+1, power+inform[cnt][position])
            visited[position] = 0


C = int(input())
for tc in range(C):
    inform = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    max_power = -float('inf')

    check_power(0, 0)
    print(max_power)