def bingo(arr, arr1):
    bingo = 0

    while bingo < 3:

        find_num(arr, arr1)
        bingo_row(arr, bingo)
        bingo_col(arr, bingo)
        bingo_cross(arr, bingo)

        if bingo == 3:
            return "으아아아아아ㅏㄱ!!!"


def find_num(arr, arr1):
    global i

    for j in range(5):
        for k in range(5):
            if bingo_arr[j][k] == shout[i]:
                bingo_arr[j][k] = -1
                i += 1
                return

def bingo_row(arr, bingo):
    cnt = 0

    for i in range(5):
        for j in range(5):
            if arr[i][j] == -1:
                cnt += 1
            else:
                break
        if cnt == 5:
            bingo += 1
        cnt = 0


def bingo_col(arr, bingo):
    cnt = 0

    for i in range(5):
        for j in range(5):
            if arr[j][i] == -1:
                cnt += 1
            else:
                break
        if cnt == 5:
            bingo += 1
        cnt = 0

def bingo_cross(arr, bingo):
    cnt = 0

    for i in range(5):
        if arr[i][i] == -1:
            cnt += 1
        else:
            break
        if cnt == 5:
            bingo += 1
        cnt = 0

    for j in range(5):
        if arr[j][4-j] == -1:
            cnt += 1
        else:
            break
        if cnt == 5:
            bingo += 1
        cnt = 0


bingo_arr = [list(map(int, input().split())) for _ in range(5)]
shout = []

for _ in range(5):
    shout.extend(map(int, input().split()))
i = 0
result = bingo(bingo_arr, shout)
print(result)