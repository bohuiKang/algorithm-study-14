from collections import deque
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

m, n, k = map(int, input().split())
# m*n 0으로 채워진 좌표 그리기
lst = [[0]*n for _ in range(m)]

# 사각형이 있는 곳에 1 삽입
# 왼쪽 아래가 (0, 0), 오른쪽 위가 (n,m)이어도 넓이 구하는데에는 상관없음
for _ in range(k):
    l_c, l_r, r_c, r_r = map(int, input().split())
    for r in range(l_r, r_r):
        for c in range(l_c, r_c):
            lst[r][c] = 1
# 넓이 반환 함수
def area(sr, sc):
    # 스택 생성, 시작점 append
    stack = deque([(sr, sc)])
    # 방문 표시
    lst[sr][sc] = 1
    # 넓이 변수 생성, 1로 시작(시작 위치 넓이 1)
    a = 1
    # dfs
    while stack:
        r, c = stack.pop()
        # 0이 있는지 델타 탐색
        for i in range(4):
            nr, nc = r+delta[i][0], c+delta[i][1]
            if 0 <= nr < m and 0 <= nc < n:
                # 0이라면 stack에 삽입
                if lst[nr][nc] == 0:
                    stack.append((nr, nc))
                    # 중복 방지
                    lst[nr][nc] = 1
                    # 넓이 갱신
                    a += 1
    return a

# 영역의 넓이를 담을 리스트
result = []
# 0을 찾아서 넣고 상하좌우 탐색, dfs, 방문시 1로 변경, 한번 순회가 끝날때마다 영역의 넓이를 result에 저장
for r in range(m):
    for c in range(n):
        if lst[r][c] == 0:
            a = area(r, c)
            result.append(a)

# 오름차순 정렬
result.sort()
# 영역 개수, 넓이 출력
print(len(result))
print(*result)

