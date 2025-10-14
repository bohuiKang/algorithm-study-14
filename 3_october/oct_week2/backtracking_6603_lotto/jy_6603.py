import sys

def recur(start, comb):
    if len(comb) == 6:
        print(*comb)
        return

    for i in range(start, k):
        recur(i + 1, comb + [lst[i]])

# input 받는 코드
all_inputs = []

for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    all_inputs.append(list(map(int, line.split())))

for input_case in all_inputs:
    k = input_case[0]
    lst = input_case[1:]
    recur(0, [])
    print()