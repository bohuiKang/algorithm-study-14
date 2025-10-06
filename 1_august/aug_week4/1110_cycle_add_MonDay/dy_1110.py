n = int(input())

num = 0
first = n
#앞자리
a = 0
#뒷자리
b = 0
#a,b 더한 후의 뒷자리
c = 0
while True:
    num += 1
    #10보다 작으면 자동으로 앞자리에 0
    a = n//10
    b = n%10
    c = (a+b)%10
    n = (b*10) + c
  
    if n == first:
        break
print(num)