N = int(input())

def new_num (num): # 새로운 수 만드는 함수
    cal_num = (num // 10 + num % 10) % 10 +( num % 10 ) * 10
    return cal_num

new_cal_num = new_num(N) # 첫 계산

cnt = 1 # 맨처음 계산은 완료 햇으므로 1부터 count (1이 최소 count 1번은 무조건 시행하기때문)
while  new_cal_num != N: # 입력해준 수와 같아지면 반복문 종료
    cnt += 1
    new_cal_num = new_num(new_cal_num)

print(cnt)