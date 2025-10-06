n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

#감소 횟수 초기화
num = 0

#역순으로 순회
for j in range(n-1, 0, -1):
    #현재가 그전것보다 낮다면 높아질때까지 반복
    while lst[j] <= lst[j-1]:
        #점수를 1점 차감하고 횟수 1증가
        lst[j-1] -= 1
        num += 1
print(num)