lst = list(input())
#스위치 누른 횟수
count = 0
#break될때까지 계속 반복
while True:
    # 꺼야되는 스위치의 번호 리스트, 반복될때마다 새로 갱신
    off_lst = []

    # 꺼야되는 스위치 탐색 for문
    for i in range(len(lst)):
        if lst[i] == 'Y':
            off_lst.append(i + 1)

    # 만약 꺼야되는 스위치가 없다면 break, 있다면 그다음 for문에서 스위치를 내릴것이기에 count += 1
    if off_lst == []:
        break
    else:
        count += 1

    # 켜진 것 중 가장 작은 값(off_lst[0])을 꺼준다.
    for j in range(len(lst)):
        #가장 작은 값의 배수인 스위치들을 반전시켜준다.
        if (j + 1) % off_lst[0] == 0:
            if lst[j] == 'Y':
                lst[j] = 'N'
            else:
                lst[j] = 'Y'