# 빙고
'''
입력: 첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

출력: 
15
'''
paper = [list(map(int, input().split())) for _ in range(5)] # 빙고판
host = [0] * 25
for num in range(0,25,5): # 사회자 호출번호 한줄로 만들기
    host[num:num+5] = map(int, input().split())

# 숫자 찾기
def find_num(h):
    for r in range(5):
        for c in range(5):
            if paper[r][c] == host[h]: # 번호가 있으면,
                paper[r][c] = 'x' # x 표시
                return
# 빙고 찾기
def find_bingo():
    bingo = 0
    
    x_check = 0 # 대각선
    rx_check = 0 # 반대 대각선
    for r in range(5):
        if paper[r][r] == 'x':
            x_check += 1
        if paper[r][4-r] == 'x':
            rx_check += 1
        r_check = 0 # 행
        c_check = 0 # 열
        for c in range(5):
            if paper[r][c] == 'x':
                r_check += 1
            if paper[c][r] == 'x':
                c_check += 1
        if r_check == 5:
            bingo += 1
        if c_check == 5:
            bingo += 1
    if x_check == 5:
        bingo += 1
    if rx_check == 5:
        bingo += 1
    # print('bingo: ', bingo)
    return bingo

for h in range(len(host)):
    find_num(h) # 숫자 체크

    if h >= 12: # 12개 이상부터 => 3빙고가 되려면 최소 12개의 숫자가 필요
        if find_bingo() >= 3: # 한 숫자에 두개 이상 빙고가 나올 수 있기에 3이상
            print(h+1)
            break
    