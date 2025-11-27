import sys; sys.stdin = open('input.txt', 'r')

def check_7(level, person, height, line):
    global ans
    if ans:
        return

    if level >= 9: # 난쟁이 수를 넘으면 return
        if person == 7 and height == 100:
            ans = line
            for i in line:
                print(i)
            return
        return

    check_7(level + 1, person + 1, height + arr[level], line + [arr[level]])
    check_7(level + 1, person, height, line)

arr = sorted([int(input()) for _ in range(9)])
ans = []

check_7(0, 0, 0, []) # 난쟁이 순번, 난쟁이 수, 난쟁이 키, 난쟁이 키순