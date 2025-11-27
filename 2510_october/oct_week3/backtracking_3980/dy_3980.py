import sys
sys.stdin = open('3980_input.txt')

tc = int(input())
for _ in range(tc):
    lst = [list(map(int, input().split())) for _ in range(11)]
    # 최대 능력치의 합
    max_a = float('-inf')
    used = [0]*11

    def recur(cnt, s):
        global max_a

        if cnt == 11:
            if max_a < s:
                max_a = s
            return

        for i in range(11):
            if not used[i]:
                if lst[i][cnt] == 0:
                    # 능력치가 0이면 배치할 수 없으니 패스
                    continue
                # 중복 방지
                used[i] = 1
                recur(cnt+1, s+lst[i][cnt])
                used[i] = 0

    recur(0, 0)
    print(max_a)




