n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

max_pay = 0
def work(start, pay):
    global max_pay

    #상담 시작일이 n과 같거나 크다면 종료
    if start >= n:
        if max_pay < pay:
            max_pay = pay
        return

    #해당 날에 상담을 했을때
    if start+lst[start][0] <= n:
        #상담종료일, pay+해당상담보수로 다시 재귀
        work(start+lst[start][0], pay+lst[start][1])
    #안했을때
    work(start+1, pay)

work(0,0)
print(max_pay)
