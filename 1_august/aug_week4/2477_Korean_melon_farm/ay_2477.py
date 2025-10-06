N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
count =[0] * 5
leng_2nd_way = []
leng_2nd_leng = []
idx = []

for i in range(6):
    way, leng = arr[i]
    
    if count[way] == 0:
        count[way] = leng
    else:
        leng_2nd_way.append(way)
        leng_2nd_leng.append(leng)
        idx.append(i)

ex_lng = []
for i in range(2):
    j = idx[i]
    if (arr[(j-1)%6][0] not in leng_2nd_way) or (arr[(j+1)%6][0] not in leng_2nd_way):
        ex_lng.append(count[leng_2nd_way[i]])
    else:
        ex_lng.append(leng_2nd_leng[i])

if 1 in leng_2nd_way: # 전체 가로 길이
    max_garo = count[2]
else:
    max_garo = count[1]

if 3 in leng_2nd_way: # 전체 세로 길이
    max_sero = count[4]
else:
    max_sero = count[3]

r, c = ex_lng


num = max_garo * max_sero - (r * c)
print(num * N)

