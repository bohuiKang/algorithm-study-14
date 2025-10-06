'''
#1m**2당 자라는 참외 개수
K = int(input())
length_lst = [list(map(int, input().split())) for _ in range(6)]
#너비의 리스트(북4,남3)
w_lst = []
#높이의 리스트(동1,서2)
h_lst = []
for i in range(6):
    if length_lst[i][0] == 1 or length_lst[i][0] == 2:
        h_lst.append(length_lst[i][1])
    else:
        w_lst.append(length_lst[i][1])

#오름차순 정렬, 가장 긴변이 육각형의 너비, 높이
h_lst.sort()
w_lst.sort()
#육각형의 넓이 = 큰 사각형 - 작은 사각형
extent = h_lst[2]*w_lst[2] - w_lst[0]*h_lst[0]
print(extent*K)
가장 작은 변이 작은 사각형이라는 보장은 없다.
'''

#1m**2당 자라는 참외 개수
K = int(input())
length_lst = [list(map(int, input().split())) for _ in range(6)]

#가장 긴변의 인덱스 찾기
h, w = 0, 0
h_idx, w_idx = 0, 0
for j in range(6):
    if length_lst[j][0] == 1 or length_lst[j][0] == 2:
        if w < length_lst[j][1]:
            w = length_lst[j][1]
            w_idx = j
    elif length_lst[j][0] == 3 or length_lst[j][0] == 4:
        if h < length_lst[j][1]:
            h = length_lst[j][1]
            h_idx = j

#작은 사각형 찾기
little_h =abs( length_lst[(h_idx + 1) % 6][1] - length_lst[(h_idx - 1) % 6][1] )
little_w = abs( length_lst[(w_idx + 1) % 6][1] - length_lst[(w_idx - 1) % 6][1] )
little_area = little_h * little_w
#육각형의 넓이 = 큰 사각형 - 작은 사각형
area = w*h - little_area
print(area*K)