'''
from collections import deque
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

n = int(input())
lst = [list(map(int, input())) for _ in range(n)]
#총 단지 수
total_n = 0
#단지별 수 목록
n_lst = [0]*625
#중복 방지, 방문 목록
visited = [[0]*n for _ in range(n)] #visited[now[0]][now[1]] = 1 이렇게 하면 오류
#스택, 방문예정목록
stack = deque()

idx = 0
#전체 열 탐색, 1을 찾으면 상하좌우 없을때(방문목록)까지 탐색
for r in range(n):
    for c in range(n):
        #방문한 적 없고 1이라면 총 단지 수 추가 후 상하좌우 없을때까지 탐색
        if lst[r][c] == 1 and visited[r][c] == 0:
            total_n += 1
            stack.append([r, c])
            visited[r][c] = 1
            while stack:
                now = stack.pop()
                n_lst[idx] += 1
                for i in range(4):
                    next_r = now[0]+delta[i][0]
                    next_c = now[1]+delta[i][1]
                    if 0 <= next_r < n and 0 <= next_c < n:
                        if lst[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
                            stack.append([next_r, next_c])
                            #방문표시를 now = stack.pop() 이 다음으로 하니까 중복된다
                            visited[next_r][next_c] = 1
            idx += 1
sorted(n_lst)
print(total_n)
for i in range(idx):
    print(n_lst[i])


    ##방문표시 위치 다르게

from collections import deque
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

n = int(input())
lst = [list(map(int, input())) for _ in range(n)]
#총 단지 수
total_n = 0
#단지별 수 목록
n_lst = [0]*625
#중복 방지, 방문 목록
visited = [[0]*n for _ in range(n)] #visited[now[0]][now[1]] = 1 이렇게 하면 오류
#스택, 방문예정목록
stack = deque()

idx = 0
#전체 열 탐색, 1을 찾으면 상하좌우 없을때(방문목록)까지 탐색
for r in range(n):
    for c in range(n):
        #방문한 적 없고 1이라면 총 단지 수 추가 후 상하좌우 없을때까지 탐색
        if lst[r][c] == 1 and visited[r][c] == 0:
            total_n += 1
            stack.append([r, c])
            while stack:
                now = stack.pop()
                if visited[now[0]][now[1]] == 0:
                    visited[now[0]][now[1]] = 1
                    n_lst[idx] += 1
                    for i in range(4):
                        next_r = now[0]+delta[i][0]
                        next_c = now[1]+delta[i][1]
                        if 0 <= next_r < n and 0 <= next_c < n:
                            if lst[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
                                stack.append([next_r, next_c])
            idx += 1

sorted(n_lst) #n_lst.sort()하면 왜 000이 나오지........가이유가 있구나 빈곳은 0이구나
print(total_n)
for i in range(idx):
    print(n_lst[i])
'''
from collections import deque
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

n = int(input())
lst = [list(map(int, input())) for _ in range(n)]
# 총 단지 수
total_n = 0
# 단지별 수 목록(그냥 n의 최대인 25의 제곱+2)
n_lst = [0]*627
#스택, 방문예정목록
stack = deque()

# 단지번호, 이미 좌표에 0과 1이 있기에 2부터 시작
idx = 2
# 전체 열 탐색, 1을 찾으면 상하좌우 없을 때(방문목록이 없어질 때)까지 탐색
# 방문 표시는 방문했을때 1을 단지번호로 갱신함으로써 표시
for r in range(n):
    for c in range(n):
        # 방문한 적 없는 1이라면 총 단지 수 증가 후 상하좌우 없을때까지 탐색
        if lst[r][c] == 1:
            total_n += 1
            stack.append([r, c])
            # 리스트에 방문표시를 위해 단지 번호로 갱신
            lst[r][c] = idx
            while stack:
                #방문 예정 목록에서 하나를 꺼내와서
                now = stack.pop()
                #단지별 개수 증가
                n_lst[idx] += 1
                # 델타를 이용하여 상하좌우 방문
                for i in range(4):
                    next_r = now[0]+delta[i][0]
                    next_c = now[1]+delta[i][1]
                    #유효성 검증
                    if 0 <= next_r < n and 0 <= next_c < n:
                        #상하좌우에 1, 즉 방문한적없고 집이 있다면
                        if lst[next_r][next_c] == 1:
                            #방문 표시 후(방문했을때 표시할려고하니까 길이가 더 길어져서 여기서 표시)
                            lst[next_r][next_c] = idx
                            #방문 예정 목록에 추가
                            stack.append([next_r, next_c])
            #while문이 끝났다, 더이상 주변에 집이 없기에 idx(단지번호)을 갱신해준다.
            idx += 1

#단지 번호가 2부터 시작하므로 2부터 idx까지 슬라이싱한 후 정렬
n_lst_sorted = sorted(n_lst[2:idx])
print(total_n)
print(*n_lst_sorted, sep='\n')
