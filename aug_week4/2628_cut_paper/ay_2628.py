import sys
sys.stdin = open("2628.txt", "r")

c, r = map(int, input().split()) # 가로 세로
N = int(input())
cut_0 = []
cut_1 = []

for i in range(N): # 가로 세로 분리하기
    rc, n = map(int, input().split())
    if rc == 0:
        cut_0.append(n)
    else:
        cut_1.append(n)

cut_0.append(r) # 마지막 지점 삽입
cut_1.append(c)

cut_0.sort() # 크기 순 정렬
cut_1.sort()


def wide(arr):
    if len(arr) == 0:
        return 1

    i = 0
    new_arr = [arr[0]]
    while i < len(arr) - 1:
        length = arr[i+1] - arr[i]
        new_arr.append(length)
        i += 1

    return new_arr


wide_0 = wide(cut_0)
wide_1 = wide(cut_1)

max_v = 0
for i in wide_0: # 두 길이 곱하면 해당 종이 크기가 됨
    for j in wide_1:
        if max_v < (i * j):
            max_v = i * j
print(max_v)