a, b = map(int, input().split())
c = list(input().split())
d = []

for i in c:
    if int(i) < b:
        d.append(str(i))

print(" ".join(d))touch