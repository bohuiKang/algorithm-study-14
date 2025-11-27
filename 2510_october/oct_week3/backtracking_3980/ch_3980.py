# 1번선수 가능한 포지션에 넣고, 2번 depth로 내려감
# 2번선수 가능한 포지션에 넣고, 3번 depth로 내려감
# 3번선수 ..... 11번 선수까지 반복
# 이미 다른 선수가 들어간 포지션은 불가
# 현재 선수가 더이상 들어갈 포지션이 없으면 return
# 모든 선수(11번까지)가 포지션을 가졌다면 능력치의 합을 출력
C = int(input())
for tc in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    result = []
    visited = [0] * 11

    def recur(num, total):
        if num == 11:
            result.append(total)
            return

        for i in range(11):
            if not arr[num][i] or visited[i]:     # 해당 포지션에 이번 선수가 들어갈 수 없으면 건너뜀
                continue
            visited[i] = 1
            recur(num + 1, total + arr[num][i])   # 다음 선수로 재귀
            visited[i] = 0

    recur(0, 0)
    print(max(result))