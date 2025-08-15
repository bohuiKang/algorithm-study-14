arr = list(input())
light = []
for i in arr:
    if i == 'Y':
        light += [1]
    else:
        light += [0]

cnt = 0
i = 0
while i < len(arr):

    if light[i] == 1:
        ni = i
        cnt += 1
        while ni < len(arr):
            light[ni] = 1 - light[ni]
            ni += i+1
        i += 1

    else:
        for j in range(i, len(arr)):
            if light[j] == 1:
                i = j
                break
        else:
            break

for i in light:
    if light[i] == 1:
        cnt = -1
        break
print(cnt)