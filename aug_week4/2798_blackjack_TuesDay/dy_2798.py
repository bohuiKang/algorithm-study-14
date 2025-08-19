n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum = 0
best = 0 #m과 가장 가까운 합
#카드 1 선택 i
for i in range(n):
  #카드 2 선택 j
  for j in range(n):
    if i != j:
      #카드 3 선택 k
      for k in range(n):
        #i,j,k 중복 방지
        if i != k and j != k:
          sum = lst[i] +lst[j] +lst[k]
          #m을 넘기지않을때
          if sum < m:
            #가장 가까운 합 찾기
            if m-best > m-sum:
              best = sum
          #m과 같다면 break  
          elif sum == m:
            best = m
            break
print(best)