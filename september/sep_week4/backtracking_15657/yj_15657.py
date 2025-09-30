# 중복 가능, 비내림차순
def recur(cnt, start):
    # 기저조건: M개 다 뽑으면
    if cnt == M:
        print(*path)
        return

    # 재귀파트
    for i in range(start, N):
        path.append(arr[i])
        recur(cnt + 1, i)  # 다음 재귀 범위: 지금부터 끝까지
        path.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 오름차순 정렬

path = []
recur(0, 0)