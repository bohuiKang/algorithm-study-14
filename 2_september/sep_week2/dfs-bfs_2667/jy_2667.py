from collections import deque

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dc = [1, 0, -1, 0]
dr = [0, 1, 0, -1]
cnt_lst = []
CNT = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            q = deque([(i, j)])
            visited[i][j] = 1
            cnt = 0

            while q:
                curr_c, curr_r = q.popleft()
                cnt += 1
                for k in range(4):
                    mc = curr_c + dc[k]
                    mr = curr_r + dr[k]

                    if 0 <= mc < N and 0 <= mr < N and arr[mc][mr] == 1 and visited[mc][mr] == 0:
                        q.append((mc, mr))
                        visited[mc][mr] = 1

            cnt_lst.append(cnt)
            CNT += 1

print(CNT)
#정렬... 정렬... 정렬... 정렬... 정렬... 정렬... 정렬... 정렬... 정렬...
for c in sorted(cnt_lst):
    print(c, sep='\n')
