# 중복 없는 순열 만들기
def recur(cnt, start):  # start: 시작 인덱스
    if cnt == M:
        print(*path)
        return
    
    # 뒤의 원소가 앞에 나온 원소보다 작을 수 없다. 같을 수는 있음
    for i in range(start, N):
        if not visited[arr[i]]:
            path.append(arr[i])
            visited[arr[i]] = 1
            recur(cnt + 1, i)
            visited[arr[i]] = 0
            path.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * 10001
path = []
recur(0, 0)