import sys

graph = []
for _ in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))

zeros = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zeros.append((i, j))

def check(r, c, num):

    # 같은 행 확인
    if num in graph[r]:
        return False
    
    # 2. 같은 열 확인
    for i in range(9):
        if graph[i][c] == num:
            return False
            
    # 3. 3x3 구역
    start_r = (r // 3) * 3
    start_c = (c // 3) * 3
    
    for i in range(3):
        for j in range(3):
            if graph[start_r + i][start_c + j] == num:
                return False
                
    return True

def dfs(idx):

    # 모든 빈칸을 다 채움
    if idx == len(zeros):
        for row in graph:
            print(*row)
        return True

    r, c = zeros[idx]
    
    for num in range(1, 10):
        if check(r, c, num):
            graph[r][c] = num
            if dfs(idx + 1):
                return True
            graph[r][c] = 0   # 다시 비워둠

dfs(0)