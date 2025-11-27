# 중복 가능, 오름차순 같은거, 수열
def recur(cnt, start, path):
    if cnt == M:
        ans_list.append(path[:])  # 깊은 복사
        return
    
    # 뒤의 원소가 앞에 나온 원소보다 작을 수 없다. 같을 수는 있음
    for i in range(start, N + 1):  
        path[cnt] = i
        recur(cnt + 1, i, path)
        path[cnt] = []

N, M = map(int, input().split())
ans_list = []
path = [[] for _ in range(M)]  # append를 안 쓰기 위해 인덱스 사용할거임
recur(0, 1, path)
for x in ans_list:
    print(*x)