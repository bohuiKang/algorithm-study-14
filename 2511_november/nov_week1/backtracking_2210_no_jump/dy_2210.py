delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n = 5
#문자열로 저장, 000123과 같은 숫자를 만들기 위해서
lst = [list(input().split()) for _ in range(n)]
# 중복 방지
result = set()

# 재귀로 완탐
def recur(r, c, cnt, string):
    # 6자리를 다 만들었다면
    if cnt == 6:
        # set에 추가
        result.add(string)
        return
    # 델타로 4방향 탐색
    for i in range(4):
        nr, nc = r + delta[i][0], c + delta[i][1]
        # 유효성 검사, 가능하다면 재귀
        if 0 <= nr < n and 0 <= nc < n:
            recur(nr, nc, cnt+1, string + lst[nr][nc])

# 모든 시작점에서 재귀 돌려보기
for r in range(n):
    for c in range(n):
        recur(r, c, 0, '')


# result에 들은 개수 출력
print(len(result))
