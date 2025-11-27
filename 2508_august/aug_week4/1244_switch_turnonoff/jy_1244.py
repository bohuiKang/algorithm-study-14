n = int(input())
lights = list(map(int, input().split()))
student_n = int(input())
turn_lst = [list(map(int, input().split())) for _ in range(student_n)]

for turn in turn_lst:
    if turn[0] == 1: #남학생
        for i in range(n):
            if turn[1] <= i+1 and (i+1)%turn[1] == 0:
                lights[i] ^= 1

    else: #여학생
        left = (turn[1]-1) - 1
        right = (turn[1]-1) + 1
        lights[turn[1] - 1] ^= 1

        while 0 <= left and right < n:
            if lights[left] == lights[right]:
                lights[left] ^= 1
                lights[right] ^= 1
                left -= 1
                right += 1
            else:
                break

for i in range(0, n, 20):
    print(*lights[i:i+20])