#가로점선, 행을 따라 자르는 경우 종이의 왼쪽 끝에서 오른쪽 끝까지
#세로 점선, 위쪽 끝에서 아래쪽 끝까지 한번에 자른다.
#칸마다 1cm**2, 값이 1인 배열
w, h = map(int, input().split())
#자르는 횟수
cut_n = int(input())
#잘라야하는 목록
cut_lst = [list(map(int, input().split())) for _ in range(cut_n)]

#전체 배열
lst = [[1]*(w) for _ in range(h)]
#가로로 잘라야하는 목록, 세로로 잘라야하는 목록, 내림차순 정렬하여 차례대로 자르기
w_cut = []
h_cut = []
for cut in cut_lst:
    if cut[0] == 0:
        w_cut.append(cut[1])
    else:
        h_cut.append(cut[1])
#테두리 값 추가
w_cut.append(0)
h_cut.append(0)
w_cut.append(h)
h_cut.append(w)
w_cut.sort()
h_cut.sort()

#자르는 목록 다 돌때까지 반복
w_c1 = 0
max_sum = 0
while True:
    w_c2 = w_c1+1
    if w_c2 == len(w_cut):
        break

    for h_c in range(len(h_cut)):
        h_c1 = h_c
        h_c2 = h_c + 1
        if h_c2 == len(h_cut):
            break
        sum = 0
        for r in range(w_cut[w_c1], w_cut[w_c2]):
            for c in range(h_cut[h_c1], h_cut[h_c2]):
                sum += lst[r][c]
        if max_sum < sum:
            max_sum = sum

    w_c1 += 1

print(max_sum)