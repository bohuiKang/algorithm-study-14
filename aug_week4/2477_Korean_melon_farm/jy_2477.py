n = int(input())

k_melon = [list(map(int, input().split())) for _ in range(6)]

w = 0
h = 0

for i in range(6):
    if k_melon[i][0] in [1, 2]: #방향별로 분류하여 h,w 최댓값 찾기
        if k_melon[i][1] > w:
            w = k_melon[i][1]
            w_idx = i
    else:
        if k_melon[i][1] > h:
            h = k_melon[i][1]
            h_idx = i

minus_w = k_melon[(h_idx + 3) % 6][1] #구조상 최대 길이 3턴 뒤에 나옴
minus_h = k_melon[(w_idx + 3) % 6][1]

print((w*h - minus_h*minus_w)*n)

