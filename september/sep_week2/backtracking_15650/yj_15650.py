# 일단 중복 없는 순열 만들기
def recur(cnt, cur_path):     # cnt: 몇 개를 뽑았는지
    # 기저조건: M개를 다 뽑았으면 끝내기
    if cnt == M:
        # todo: sorted(path)하고 ans_list에 추가하기
        path = sorted(cur_path)     # 오름차순 정렬
        # ans_list에 없을때만 append
        if path not in ans_list:
            ans_list.append(path[:])
            print(*path)
        return

    # 재귀 파트
    for i in range(1, N + 1):
        if not visited[i]:
            cur_path.append(i)
            visited[i] = 1
            recur(cnt + 1, cur_path)
            cur_path.pop()
            visited[i] = 0

N, M = map(int, input().split())
path = []
visited = [0] * (N + 2)
ans_list = []
recur(0, [])