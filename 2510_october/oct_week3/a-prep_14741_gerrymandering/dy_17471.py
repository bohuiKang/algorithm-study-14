from collections import deque
from itertools import combinations

# 지역구 수
n = int(input())
# 인구 정보 리스트
p_lst = list(map(int, input().split()))
# 인접 정보 리스트, 인덱스 0은 인접 구역의 수, 인접 정보는 인덱스+1로 나타나있음(1~n구역)
n_lst = [list(map(int, input().split())) for _ in range(n)]
# 최소값
min_p = float('inf')


# 연결되었는지 확인하는 함수
# 연결되었으면 인구수 반환, 아니라면 -1 반환
def is_c(group, size):
    # 방문 예정 목록 stack
    s = deque()
    # 방문 확인 목록
    visited = [0] * n
    # 방문한 구역 수
    cnt = 0
    # 인구수 합계
    p = 0
    # 그룹의 첫번째 구역 방문 예정, 방문한 구역 수 + 1, 방문 확인 갱신
    s.append(group[0])
    cnt += 1
    visited[group[0]] = 1
    p += p_lst[group[0]]
    while s:
        # dfs로 탐색
        now = s.pop()
        for i in range(1, n_lst[now][0] + 1):
            # 현재 인덱스값으로 접근중이기에 인접리스트 값의 -1
            next = n_lst[now][i] - 1
            # 만약 인접 구역이 해당 구역에 있고
            if next in group:
                # 방문한적 없다면 방문 예정 목록에 추가하고 구역수, 인구수 갱신
                if visited[next] == 0:
                    s.append(next)
                    cnt += 1
                    visited[next] = 1
                    p += p_lst[next]
    # 방문한 구역 수와 구역의 크기가 같다면 모두 연결된 것이기에 인구수 반환
    if size == cnt:
        return p
    # 다르다면 모두 연결된것이 아니기에 -1 반환
    return -1


# 가능한 조합
for i in range(1, n // 2 + 1):
    # 첫번째 구역 선택
    for f in combinations(range(n), i):
        first = list(f)
        # 첫번째 구역으로 선택된 것들이 모두 연결되었는지 확인
        f_result = is_c(first, i)
        if f_result == -1:
            continue
        # 연결되어 if에 걸리지 않는다면 두번째 구역 확인
        second = []
        # 구역 전체 순회, first에 없다면 두번째 구역에 추가
        for j in range(n):
            if j not in first:
                second.append(j)
        # 연결 확인
        s_result = is_c(second, n-i)
        if s_result == -1:
            continue
        # 모두 연결되었다면 최소값 갱신
        min_p = min(min_p, abs(f_result - s_result))

# 최소값이 갱신된적 없다면 두 선거구로 나눌 수 없는 경우이기에 -1 출력
if min_p == float('inf'):
    print(-1)
# 갱신된적 있다면 최소값 출력
else:
    print(min_p)
