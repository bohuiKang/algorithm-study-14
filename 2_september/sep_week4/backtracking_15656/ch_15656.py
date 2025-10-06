# 중복가능 N개 숫자중 M개 고른 수열
N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

def recur(depth, path):
    if depth == M:  # 기저조건: M개를 고르면 출력 후 종료
        print(*path)
        return
    for num in range(N):    # N개 숫자중에 하나 골라서 다음 재귀로
        recur(depth + 1, path+[arr[num]])

recur(0, [])