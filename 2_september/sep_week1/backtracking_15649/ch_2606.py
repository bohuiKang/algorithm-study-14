# 중복없음, 수열을 공백으로 하나씩 출력
N, M = map(int, input().split()) # N: 1 ~ N까지의 자연수, M: 수열에 포함될 숫자의 개수
visited = [0] * (N + 1)
path = []
def recur(depth):
    global cnt
    if depth == M:
        print(*path)
        return
    
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = 1
        path.append(i)
        recur(depth + 1)
        visited[i] = 0
        path.pop()

recur(0)
