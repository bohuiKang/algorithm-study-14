A = int(input())
B = int(input())
C = int(input())

mult = A * B * C
count = [0]*10
while mult > 10:
    num = mult % 10
    mult = mult // 10
    count[num] +=1

count[mult] += 1
for i in range(10):
    print(count[i])