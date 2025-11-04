from collections import deque

# 입력
N, K = map(int, input().split())
size = 10**5+2
# x-1, x+1의 무한 루프 제거, 중복 계산 제거 위해 visited 사용
# visited를 통해 각 위치를 최대 한번씩만 큐에서 꺼내 처리
'''
ex) 출발점이 0일 때,
    0 * 2 => 0 -> 계속해서 *2를 곱하게 됨
    0 + 1 => 1, 1 - 1 => 0 의 무한루프 제거 필요
    1 + 1 => 2, 1 * 2 => 2 의 중복 위치 계산 제거
'''
# 1e6: 지수 표기법 => 1000000.0 <class 'float'>
visited = [False] * size
q = deque()

# 음수이면 수빈이가 동생보다 앞에 있는 것
# 0이면 수빈이와 동생이 현재 같은 위치에 있는 것
gap = K - N

if gap <= 0:  # 수빈이가 뒤로만 이동해야 할 때,
    min_time = abs(gap)
else:
    # +1, -1, *2 순으로 BFS
    min_time = float('inf')
    q.append((N, 0))  # 위치와 time
    visited[N] = True

while q:
    X, time = q.popleft()

    if X == K:  # 순간이동하는 수빈이가 동생을 잡음
        min_time = min(min_time, time)
        break

    for i in (X + 1, X - 1, X * 2):
        if i < 0 or i >= size or visited[i]:  # 메모리초과 처리
            continue
        q.append((i, time + 1))
        visited[i] = True

# 출력
print(min_time)