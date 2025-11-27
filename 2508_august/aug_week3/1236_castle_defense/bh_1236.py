# 성 지키기
'''
영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 
영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.
성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에는 성의 상태가 주어진다. 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.
3 5
XX...
.XX..
...XX

5 8
....XXXX
........
XX.X.XX.
........
........

2 1
.
X


출력: 첫째 줄에 추가해야 하는 경비원의 최솟값을 출력한다.
0

3

0
'''

N, M = map(int, input().split()) # 성의 세로, 가로
castle = [list(map(str, input())) for _ in range(N)]

# add_watchman = 0
# for r in range(N):
    
#     for c in range(M):
#         if castle[r][c] == 'X':
#             break

#     else: # 이번 행에 경비원이 없을 때, 
#         for cc in range(M): # 각 행의 열 줄에 경비원이 있는지 확인,

#             check_watchman = 0
#             for rr in range(N): # 현재 열번호의 전체 행의 경비원으로 조회

#                 if castle[rr][cc] == 'X': # 경비원이 있으면, 
#                     check_watchman += 1 # +1 하고 for 문 종료
#                     break

#             if check_watchman == 0: # 해당 열의 행에 경비원이 없을 때 
#                 castle[r][cc] = 'X'
#                 add_watchman += 1
#                 break

#         else: # 모든 열에 경비원이 있고 이번 행에만 경비원이 없을 때 행의 맨 처음 열에 경비원 배치
#             if M != 1:
#                 castle[r][c] = 'X'
#                 add_watchman += 1


max_watchman = 0
empty_watchman = 0
for r in range(N):
    for c in range(M):
        if castle[r][c] == 'X':
            break
    else: # 이 행에 경비원이 없을 때
        empty_watchman += 1

if max_watchman < empty_watchman:
    max_watchman = empty_watchman        

empty_watchman = 0
for c in range(M):
    for r in range(N):
        if castle[r][c] == 'X':
            break
    else: # 이 열에 경비원이 없을 때
        empty_watchman += 1

if max_watchman < empty_watchman:
    max_watchman = empty_watchman     

print(max_watchman)
