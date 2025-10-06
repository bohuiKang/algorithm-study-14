def recur(cnt, height, start):
    global is_ans
    
    if is_ans == 1: return  # 첫 답이 출력됐으면 나가기

    # 기저조건
    if cnt == 7 and height == 100 and is_ans == 0:  # 7개 난쟁이의 키의 합이 100인 첫 케이스 출력
        for a in path:
            print(a)
        is_ans = 1
        return

    # 만약 합이 100이 넘거나 같으면 pass
    if height >= 100:
        return

    # 재귀
    for i in range(start, len(arr)):
        if not visited[i]:
            path.append(arr[i])
            visited[i] = 1
            recur(cnt + 1, height + arr[i], start + 1)
            path.pop()
            visited[i] = 0

arr = []
for i in range(9):
    tmp = int(input())
    arr.append(tmp)
arr.sort()  # 오름차순 정렬

path = []
visited = [0] * 9
is_ans = 0
recur(0, 0, 0)