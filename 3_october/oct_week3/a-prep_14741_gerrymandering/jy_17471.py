from itertools import combinations
from collections import deque

def is_connected(group):
    q = deque([next(iter(group))])
    visited = set([next(iter(group))])
    while q:
        curr = q.popleft()
        for nxt in neighbor[curr]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return visited == group

N = int(input())
population = list(map(int, input().split()))
neighbor = [[] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for x in temp[1:]:
        neighbor[i].append(x - 1)

answer = float('inf')
for i in range(1, N // 2 + 1):
    for comb in combinations(range(N), i):
        groupA = set(comb)
        groupB = set(range(N)) - groupA
        if is_connected(groupA) and is_connected(groupB):
            sumA = sum(population[j] for j in groupA)
            sumB = sum(population[j] for j in groupB)
            answer = min(answer, abs(sumA - sumB))

print(-1 if answer == float('inf') else answer)
