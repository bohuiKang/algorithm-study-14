ABC = list(map(int, input().split()))
# abc = ['A', 'B', 'C']

max_v = ABC[0]
for i in range(2, 0, -1):
    for j in range(i):
        if ABC[j] > ABC[j+1]:
            ABC[j], ABC[j+1] = ABC[j+1], ABC[j]
            # abc[j], abc[j+1] = abc[j+1], abc[j]

print(ABC[1])

