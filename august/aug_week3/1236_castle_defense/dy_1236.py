n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

num_r = 0 #추가해야하는 경비원의 최솟값
#행을 도는 for 문
for i in range(n):
  #특정 행의 경비원 수
  n_r = 0
  #기준 행의 열을 도는 for 문
  for j in range(m):
    if lst[i][j] == 'X':
        n_r += 1
  if n_r == 0:
    num_r += 1

num_c = 0
#열을 도는 for문
for k in range(m):
    n_c = 0
    for l in range(n):
        if lst[l][k] == 'X':
            n_c += 1
    if n_c == 0:
        num_c += 1

#빈 열/행이라면 모든 행/열에 세워놓을 수 있기에 행과 열 중 더 많이 빈 곳을 채우면 
# 자동으로 적은 곳은 채워진다.
num = 0
if num_c > num_r:
    num = num_c
else:
    num = num_r
print(num)