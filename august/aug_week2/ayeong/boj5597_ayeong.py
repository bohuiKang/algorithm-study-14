count = [0] * 30

for i in range(28):
    count[int(input())-1] = 1

for i in range(30):
    if count[i] == 0:
        print(i+1)