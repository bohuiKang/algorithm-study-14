# 바이러스
import sys; sys.stdin = open('2606_input.txt')

def recur(node):
    global cnt
    # global visited

    # if not com[node]: # 노드에 뭐가 없으면 리턴
    #     return

    for nxt in range(len(com[node])):
        if visited[com[node][nxt]]:
            continue
        visited[com[node][nxt]] = 1
        cnt += 1
        recur(com[node][nxt])

N = int(input()) # 컴퓨터 수
M = int(input()) # 간선 수
com = [[] for _ in range(N + 1)]

visited = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

cnt = 0
visited[1] = 1
recur(1)

# print(visited)
# print(com)
print(cnt)