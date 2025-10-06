# 일곱 난쟁이
arr = [0] * 9
for i in range(9):
    arr[i] = int(input())

visited = [0] * 9
result = []
def recur(depth, total, path):
    global result
    if depth == 7 and total == 100:  # 기저조건: 7명의 난쟁이를 찾은 경우
        path.sort()
        if path in result:  # 중복 제거
            return
        result.append(path)
        return
    if total > 100: # 가지치기: 현재 키의 합이 100을 넘어가는 경우
        return
    for i in range(9):
        if visited[i]:
            continue
        visited[i] = 1
        recur(depth + 1, total + arr[i], path + [arr[i]])
        visited[i] = 0

recur(0, 0, [])
for i in result[0]:
    print(i)