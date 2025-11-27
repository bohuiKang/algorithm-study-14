# 앞뒤 중복 가능 수열
def recur(cnt):
    if cnt == M:
        ans_list.append(path[:])
        return
    
    for i in range(N):
        if not visited[arr[i]]:  # visit했으면 pass
            path[cnt] = arr[i]
            visited[arr[i]] = 1
            recur(cnt + 1)
            path[cnt] = []
            visited[arr[i]] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 입력받은 수열을 sort하기 -> ans_list에 오름차순으로 들어갈거임
path = [[] for _ in range(M)]
visited = [0] * 10001  # 자연수의 최대 값까지 초기화
ans_list = []
recur(0)
for x in ans_list:
    print(*x)