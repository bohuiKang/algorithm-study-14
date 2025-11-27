square = list(map(int, input().split()))

tc = int(input())

w_cut = [0, square[0]]
h_cut = [0, square[1]]

for i in range(tc):
    a, b = map(int, input().split())
    if a == 0:
        h_cut.append(b)
    else:
        w_cut.append(b)

h_cut.sort()
w_cut.sort()

max_h = 0
max_w = 0

for j in range(len(h_cut)-1):
    h1, h2 = h_cut[j], h_cut[j+1]
    if abs(h1-h2) > max_h:
        max_h = abs(h1-h2)

for k in range(len(w_cut)-1):
    w1, w2 = w_cut[k], w_cut[k+1]
    if abs(w1-w2) > max_w:
        max_w = abs(w1-w2)

print(max_w * max_h)