N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]


for try_inv in range(M):
    change = []
    i, j = map(int, input().split())
    for idx in range(j-1,i-2,-1):
        change.append(arr[idx])

    for num in change:
        arr[i-1] = num
        i += 1

print(*arr)
