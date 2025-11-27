while True:
    lst = list(map(int, input().split()))
    #첫번째 입력값이 0일때 종료
    if lst[0] == 0:
        break
    #lst[0] = k개, 1부터 k까지 숫자
    k = lst[0]
    lst = lst[1:]
    lst.sort()
    path = [0]*6
    def recur(cnt, idx):
        if cnt == 6:
            print(*path)
            return

        for i in range(idx, k):
            #시작할때 6자리가 안나올것같은 경우 return
            if cnt == 0:
                if i > k-6:
                    return
            path[cnt] = lst[i]
            recur(cnt + 1, i+1)
    recur(0, 0)
    #각 테스트 케이스 사이에는 공백 필요
    print()
