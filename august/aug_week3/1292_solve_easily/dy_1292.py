a, b = map(int, input().split())
#수열 리스트 만들기
lst = []
i = 1
while len(lst) <= b:
    lst += [i]*i
    i += 1
    
s = 0
#순서는 인덱스보다 1 크기에 a-1부터 b-1까지
for k in range(a-1, b):
  s += lst[k]
#sum = lst[a-1:b]
print(s)