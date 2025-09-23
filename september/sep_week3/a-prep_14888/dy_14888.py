n = int(input())
lst = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_result = float('-inf')
min_result = float('inf')


def calcul(cnt, result):
    global max_result, min_result

    # n-1번 연산시 종료
    if cnt == n:
        if max_result < result:
            max_result = result
        if min_result > result:
            min_result = result
        return

    #연산
    for i in range(4):
        if operator[i] == 0:
            continue
        # 해당 연산자를 쓸 계획이니 감소
        operator[i] -= 1
        # 연산을 위한 복사값 생성
        n_r = result
        # 연산 진행
        if i == 0:
            n_r += lst[cnt]
        elif i == 1:
            n_r -= lst[cnt]
        elif i == 2:
            n_r *= lst[cnt]
        else:
            #음수 나눗셈의 반올림을 하지 않기 위해
            n_r = int(n_r / lst[cnt])
        # 다음 연산 진행
        calcul(cnt+1, n_r)
        # 호출 종료 후 초기화
        operator[i] += 1





# 첫번째 값 넣고 시작
calcul(1, lst[0])
print(max_result)
print(min_result)