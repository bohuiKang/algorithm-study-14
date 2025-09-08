N = int(input())    # N: 최대 일자
arr = []
for i in range(1, N + 1):
    Ti, Pi = map(int, input().split())  # Ti: 소요기간, Pi: 금액
    # arr: 소요기간, 금액이 튜플로 들어있는 카운팅 배열 / i번째 요소는 i일의 상담정보
    arr.append((Ti, Pi))

arr = [0] + arr    # 카운팅 리스트로 쓰기 위해 0번 인덱스 요소를 더해줌

max_v = float('-inf')

def recur(start, total):
    global max_v
    max_v = max(max_v, total)

    for i in range(start, N + 1):
        if i + arr[i][0] > N + 1:   # 시작일자 + 상담기간이 최대일자를 초과하면 선택 x
            continue
        # 다음 시작일자 = 선택한 상담 일자 + 선택한 상담의 기간
        recur(i + arr[i][0], total + arr[i][1])

recur(1, 0)

print(max_v)