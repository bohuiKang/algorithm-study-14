N = int(input())
cnt = 0
num = N

while True:
    cnt += 1
    ten = num // 10; one = num % 10
    num = one * 10 + ((ten+one) % 10)
    if num == N:
        break

print(cnt)