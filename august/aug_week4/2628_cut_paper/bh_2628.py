# 종이 자르기
'''
점선을 따라 이 종이를 칼로 자르려고 한다. 
가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다. 
예를 들어, <그림 1>의 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 
그리고 2번 가로 점선을 따라 자르면 <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.

입력: 첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 
둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 
가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 
입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.
10 8
3
0 3
1 4
0 2

출력: 첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.
30

'''

### 첫번째 풀이

# width, length = map(int, input().split()) # 가로, 세로
# cuts = int(input()) # 자르는 개수
# cut_num = [list(map(int, input().split())) for _ in range(cuts)]

# width_lst = [0] * (width + 1)
# length_lst = [0] * (length + 1)

# # 가로 
# for i in range(width + 1):
#     width_lst[i] = i
# # 세로
# for i in range(length + 1):
#     length_lst[i] = i

# # 잘린 종이 체크
# for i in range(cuts):
#     if cut_num[i][0] == 0: # 가로로 절단 => 세로의 값이 변동
#         for j in range(width+1):
#             if cut_num[i][1] == length_lst[j]: # 자를 위치와 리스트 원소 값이 동일할때
#                 length_lst.insert(j, cut_num[i][1]) # 자를 위치 값을 insert
#                 break
#     else: # 세로로 절단 => 가로의 값이 변동
#         for j in range(length+1):
#             if cut_num[i][1] == width_lst[j]:
#                 width_lst.insert(j, cut_num[i][1])
#                 break

# # print(width_lst)
# # print(length_lst)

# # 긴 종이 길이 찾기 => 실패
# long_width = 0
# for i in range(len(width_lst)):
#     start = i
#     for 

# long_length = 0

### 두번째 풀이

width, length = map(int, input().split()) # 가로, 세로
cuts = int(input()) # 자르는 개수
cut_num = [list(map(int, input().split())) for _ in range(cuts)]


width_lst = [0, width] # 자를 위치
length_lst = [0, length] # 자를 위치

# 잘린 종이 체크
for i in range(cuts):
    if cut_num[i][0] == 0: # 가로로 절단 => 세로의 값이 변동
        length_lst.append(cut_num[i][1])

    else: # 세로로 절단 => 가로의 값이 변동
        width_lst.append(cut_num[i][1])

width_lst.sort()
length_lst.sort()

# 긴 종이 길이 찾기
long_width = 0
start = 0
for i in range(1, len(width_lst)):
    if long_width < width_lst[i] - start:
        long_width = width_lst[i] - start
    start = width_lst[i]

long_length = 0
start = 0
for i in range(1, len(length_lst)):
    if long_length < length_lst[i] - start:
        long_length = length_lst[i] - start
    start = length_lst[i]

print(long_width * long_length)