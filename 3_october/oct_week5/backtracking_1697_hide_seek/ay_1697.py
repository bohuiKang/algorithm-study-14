import sys
sys.stdin = open("1697_input.txt", "r")

N, K = map(int, input().split()) # 수빈, 동생
# 순간이동은 오른쪽으로만
# 동생이 왼쪽에 있으면 N > K 시간 N-K
# 동생이 오른쪽에 있으면 (N < K)
# 2 * N 을 하거나 , x-1 , x+1 하기

best = [float('inf')]*100001
def rec(N, time): # 초기 N < K인 경우 최단 시간 찾는 함수
    global min_time, abs_NK
    if N == K: # K 일치시 값 비교
        min_time = time
        return

    if time == min_time: # 현재까지 시간이 min_time과 같으면 더이상 탐색할 필요 없음
        return

    if time == abs_NK: # 초기 둘사이 값보다 크면 더이상 탐색할 필요 없음
        return

    if N < 0 or N > 100000: # 범위 초과시 종료
        return

    rec(2 * N, time + 1)
    rec(N - 1, time + 1)
    rec(N + 1, time + 1)


def check_time(N, K):
    global min_time, abs_NK
    abs_NK = abs(N-K)
    min_time = abs_NK

    if N >= K:
        min_time = abs_NK
        return
    if N < K:
        rec(N, 0)

check_time(N, K)
print(min_time)





