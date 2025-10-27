# from pprint import pprint
from collections import deque


def check_empty(point):
    area_cnt = 1
    q = deque([point])
    # print(f'q : {q}')
    while q:
        rm, rn = q.popleft()
        # print(f'rm=>{rm}, rn=>{rn}')
        for dm, dn in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            zm = rm + dm
            zn = rn + dn
            if 0 <= zm < M and 0 <= zn < N:
                if arr[zm][zn] == 0:
                    area_cnt += 1
                    arr[zm][zn] = 1
                    q.append((zm, zn))
    return area_cnt


M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
# print(arr)

areas = []
for area in range(K):
    areas.append(list(map(int, input().split())))

for sm, sn, em, en in areas:
    for i in range(sm, em):
        for j in range(sn, en):
            arr[j][i] = 1

# pprint(arr)
cnt = 0
area_size = []
for mm in range(M):
    for nn in range(N):
        if arr[mm][nn] == 0:
            cnt += 1
            arr[mm][nn] = 1
            area_size.append(check_empty((mm, nn)))

area_size.sort()
print(cnt)
print(*area_size)