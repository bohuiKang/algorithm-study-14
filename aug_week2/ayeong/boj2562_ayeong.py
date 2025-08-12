num = []

for i in range(9):
    num.append(int(input()))

max_val = 0

for i in range(9):
    if max_val < num[i]:
        max_val = num[i]
        max_idx = i+1 # 최대값이 포함된 순서

print(max_val)
print(max_idx)