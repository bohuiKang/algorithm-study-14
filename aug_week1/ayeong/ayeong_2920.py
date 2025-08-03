note = list(map(int, input().split()))
des = 0
asc = 0

for i in range(7):
    val = note[i+1]-note[i]

    if val == 1:
        asc +=1                
    elif val == -1:
        des +=1
    else:
        break
                
if asc == 7:
    print('ascending')
elif des == 7:
    print('descending')
else:
    print('mixed')