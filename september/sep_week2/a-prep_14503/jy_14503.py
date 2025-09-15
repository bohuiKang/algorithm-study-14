direction = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}

def clean(cc, cr, cur_heading):
    global cnt

    #현재 칸이 청소되지 않은 경우
    if arr[cc][cr] == 0:
        arr[cc][cr] = -1
        cnt += 1

#현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for i in range(3, -1, -1):
        dir = direction.get((cur_heading + i) % 4)
        mc = cc + dir[0]
        mr = cr + dir[1]

        if 0 <= mc < N and 0 <= mr < M and arr[mc][mr] == 0:
            clean(mc, mr, (cur_heading + i) % 4)
            return  #return 안넣음 틀려...

#현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        mc = cc + direction[cur_heading][0] * (-1)
        mr = cr + direction[cur_heading][1] * (-1)

        if arr[mc][mr] == 1:
            return
        else:
            clean(mc, mr, cur_heading)

N, M = map(int, input().split())
c, r, heading = map(int, input().split())
cnt = 0

arr = [list(map(int, input().split())) for _ in range(N)]
clean(c, r, heading)

print(cnt)

