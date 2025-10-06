# 중복 가능 수열, 오름차순 출력
def recur(cnt):
    # 기저조건: M개 뽑으면 stop
    if cnt == M:
        print(*path)
        return

    # 재귀 파트
    for i in range(N):  # 모든 경우의 수 하나씩 넣어보기
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 미리 오름차순으로 정렬하기
path = []
recur(0)