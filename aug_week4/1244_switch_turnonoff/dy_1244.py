#스위치 개수
s_n = int(input())
#스위치 1 ~ N개, 1은 켜져있음 / 0은 꺼져있음
#번호 = 인덱스+1
lst = list(map(int, input().split()))
#학생 수
st_n = int(input())
#s_lst[i][0] = 학생의 성별(1 = 남, 2 = 여) s_lst[i][1] = 학생이 받은 수
s_lst = [list(map(int, input().split())) for _ in range(st_n)]

for i in range(st_n):
    student = s_lst[i][0]
    num = s_lst[i][1]
    # 남학생 - 자기 받은 수의 배수라면 스위치의 상태를 바꾼다
    if student == 1:
        for j in range(1, s_n+1):
            if j%num == 0:
                if lst[j-1] == 1:
                    lst[j-1] = 0
                else:
                    lst[j-1] = 1
    else:
    # 여학생 - 자기가 받은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
    # 가장 많은 스위치를 포함 하는 구간에 속하는 스위치의 상태를 모두 바꾼다
    # 이때 속한 스위치의 개수는  항상 홀수
    # 일단 중앙값의 스위치 상태를 변환
        if lst[num - 1] == 1:
            lst[num - 1] = 0
        else:
            lst[num - 1] = 1
        #왼쪽값 변수, 오른쪽 값 변수
        left = (num-1)-1
        right = (num-1)+1
        #유효성 검증
        if 0 <= left and right <= s_n-1:
            #좌우가 대칭이라면
            if lst[left] == lst[right]:
                #대칭이지 않을때까지 스위치 변환
                while lst[left] == lst[right]:
                    if lst[left] == 0:
                        lst[left] = 1
                        lst[right] = 1
                    else:
                        lst[left] = 0
                        lst[right] = 0
                    left -= 1
                    right += 1
                    if 0 > left or right > s_n - 1:
                        break
#20개씩 출력
for p in range(s_n):
    if (p+1)%20 == 0:
        print(lst[p])
    elif p == s_n-1:
        print(lst[p])
    else:
        print(lst[p], end=' ')