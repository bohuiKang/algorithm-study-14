# 난쟁이들 키 리스트
lst = [0]*9
for i in range(9):
    lst[i] = int(input())

#중복 체크
used = [0]*9

# 일곱난쟁이 리스트
short = [0]*7

def find(h_sum, cnt, slst):
    if cnt == 7:
        if h_sum == 100:
            return slst
        else:
            return

    if h_sum > 100:
        return

    for j in range(9):
        if not used[j]:
            slst[cnt] = lst[j]
            used[j] = 1
            result = find(h_sum+lst[j], cnt+1, slst)
            used[j] = 0
            if result:
                return result

real = find(0,0,short)
real.sort()

print(*real, sep='\n')