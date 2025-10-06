n = int(input())
line = int(input())

child_lst = [[] for _ in range(n+1)]
for _ in range(line):
    a, b = map(int, input().split())
    #양방향 리스트이기에
    child_lst[a].append(b)
    child_lst[b].append(a)

#방문예정목록
visited_lst = [1]
#이미 방문한 목록
used_lst = [-1]*(n+1)
#바이러스 걸린 컴퓨터 수
cnt = 0
#방문예정목록이 다 사라질때까지
while visited_lst:
    now = visited_lst.pop()
    #방문한적없는 곳이라면
    if used_lst[now] == -1:
        #방문 표시
        used_lst[now] = 0
        #바이러스 걸린 컴퓨터 수 추가
        cnt += 1
        #다음 갈 목록 생성
        visited_lst += child_lst[now]


#1번 컴퓨터 빼고 출력
print(cnt-1)
