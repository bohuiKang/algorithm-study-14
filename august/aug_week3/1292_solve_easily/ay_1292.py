A, B = map(int, input().split())

arr = []
i = 0
while len(arr) < B+1:
    i += 1
    for j in range(i):
        arr.append(i)
sum = 0
for i in range(A-1, B):
    sum += arr[i]


print(sum)