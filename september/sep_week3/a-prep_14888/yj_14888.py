def recur(cnt, cur_sum, plus, minus, mul, div):
    # 고른 숫자의 개수(==다음 고를 숫자의 인덱스), 현재까지의 합, 연산자들의 남은 개수
    global min_sum, max_sum

    # 기저조건
    if cnt == N:
        # 최저, 최소 갱신
        min_sum = min(min_sum, cur_sum)
        max_sum = max(max_sum, cur_sum)
        return

    # 사칙연산 재귀
    if plus > 0:
        recur(cnt + 1, cur_sum + num_list[cnt], plus - 1, minus, mul, div)
    if minus > 0:
        recur(cnt + 1, cur_sum - num_list[cnt], plus, minus - 1, mul, div)
    if mul > 0:
        recur(cnt + 1, cur_sum * num_list[cnt], plus, minus, mul - 1, div)
    if div > 0:  # 문제에 적힌 방법대로 나눗셈 하기
        if cur_sum >= 0:
            recur(cnt + 1, cur_sum // num_list[cnt], plus, minus, mul, div - 1)
        else:
            tmp = -(abs(cur_sum) // num_list[cnt])
            recur(cnt + 1, tmp, plus, minus, mul, div - 1)


N = int(input())
num_list = list(map(int, input().split()))  # 수 리스트
op_list = list(map(int, input().split()))  # 연산자 개수 리스트 (+, -, *, / 순서)
min_sum, max_sum = 1e10, -1e10

recur(1, num_list[0], op_list[0], op_list[1], op_list[2], op_list[3])

print(max_sum)
print(min_sum)