def recur(pos, total):  # 현재 뽑을 position, 현재까지의 total sum
    global answer

    # 기저조건
    if pos == 11:
        # todo: 최댓값 갱신
        answer = max(answer, total)  # 모든 포지션을 채웠을 때 최대값 갱신
        return

    # 재귀 파트
    for player in range(11):  # 플레이어 한 명씩 현재 포지션에 넣어보기
        if not visited[player] and board[player][pos] > 0:  # 이미 포지션이 정해졌거나 능력치가 0이면 continue
            visited[player] = 1  # 플레이어의 포지션이 정해짐
            recur(pos + 1, total + board[player][pos])  # 다음 포지션 재귀 돌기
            visited[player] = 0  # 백트래킹

T = int(input())
for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(11)]
    answer = 0  # 능력치의 합의 최댓값
    visited = [0] * 11  # 선수가 뽑혔는지 여부
    recur(0, 0)
    print(answer)