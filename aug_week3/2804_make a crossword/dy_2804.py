a, b = input().split()
n = len(a)
m = len(b)

lst = [['.']*n for _ in range(m)]

a_idx = -1
b_idx = -1
for i in range(n):
    for j in range(m):
        #i와 j는 모두 앞에서부터 돌기에 처음 발견한 i,j가 가장 앞에 있는 동일한 글자, 
        # 발견시 break
        if a[i] == b[j]:
            a_idx = i
            b_idx = j
            break
    if a_idx != -1:
        break

a_letter = 0
for k in range(n):
    # 행방향인 a글자 표에 넣기, j열에 들어가야함
    lst[b_idx][k] = a[a_letter]
    a_letter += 1


b_letter = 0
for l in range(m):
    # 행방향인 b글자 표에 넣기, i열에 들어가야함
    lst[l][a_idx] = b[b_letter]
    b_letter += 1
    
#출력 조심, 공백없이 출력
for ls in lst:
    print(*ls, sep='')