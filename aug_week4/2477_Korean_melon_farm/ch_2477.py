'''
남,북 방향중 제일 긴변 * 동,서 방향중 제일 긴변 = 바깥 사각형
제일 긴 가로 세로가 두번 나오면 그 다음 다음번이 안쪽 사각형의 변
'''
K = int(input())    # 1m^2당 참외 수
max_r = max_c = 0
square = []
for _ in range(6):
    direction, length = map(int, input().split())
    square.append(length)
    if direction == 1 or direction == 2:
        max_r = max(max_r, length)
    else:
        max_c = max(max_c, length)

square *= 3
for i in range(12):
    if (square[i] == max_r or square[i] == max_c) and (square[i+1] == max_r or square[i+1] == max_c):
        min_r = square[i+3]; min_c = square[i+4]
area = max_r * max_c - min_r * min_c
result = area * K
print(result)