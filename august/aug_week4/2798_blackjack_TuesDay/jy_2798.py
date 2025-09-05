#n은 카드의 개수, m은 딜러가 외치는 숫자입니다.
n, m = map(int, input().split())

#cards는 현재 놓여진 카드입니다.
cards = list(map(int, input().split()))

#limit은 카드의 합과 m의 차이값 중 최소값을 저장해놓는 변수입니다.
limit = 100000
#result는 최종적으로 출력된 카드 3장의 합을 저장해놓는 변수입니다.
result = 0

#카드는 총 3장으로 고정되어 있기에 그냥 for문을 3번 돌려 카드의 조합을 찾았습니다.
for i in range(n-2): #뒤에 있는 j와 k와의 범위 중복을 막기 위해 n-2로 범위를 조정합니다.
    for j in range(i+1, n-1): #i와 같은 이유로 n-1로 범위를 조정합니다. 또한, 앞서 i와의 중복을 막기 위해 i+1을 시작지점으로 잡아주었습니다. (i로 하면 겹치니까요)
        for k in range(j+1, n): #이전에 서술된 이유와 같습니다.
            card_sum = cards[i] + cards[j] + cards[k] #카드 세 장의 합이 card_sum에 저장됩니다.

            # dis는 m와 카드값의 차이값을 저장하는 변수입니다.
            dis = m - card_sum
            # 결과가 될 수 있는 조건은 두 가지 입니다. 먼저 3장의 합이 m보다 작거나 같은 경우,
            # 그리고 제일 최근 저장된 dis(m에 가장 가까운 카드 3장의 합과 m의 차이)보다 더 작은 경우입니다.
            if card_sum <= m and dis < limit:
                #조건에 만족하면 result와 limit에 값을 저장해두어 끝까지 비교를 진행합니다.
                result = card_sum
                limit = dis

#결과를 출력합니다.
print(result)