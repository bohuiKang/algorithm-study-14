n = int(input())
lst = list(map(int, input().split()))
#인덱스
i = 0
#최대 높이
max_high = 0
#인덱스 i가 n보다 작을때 반복
while i < n:
    #i보다 그 다음 높이가 높아진다면
  if i+1 < n and lst[i+1] -lst[i] > 0:
      #높이 변수 초기화
    high = 0
      #높이가 높아지는 동안 반복, 높이를 계속 갱신
    while lst[i+1] -lst[i] >0:
      high += lst[i+1] -lst[i]
      i = i+1
      #i+1이 초과된다면 break
      if i+1 == n:
        break
    #while문이 다 돌았다면 최대 높이와 비교
    if max_high < high:
      max_high = high

    #그다음 위치가 지금보다 높지 않다면 넘어간다
  else:
    i += 1
print(max_high)