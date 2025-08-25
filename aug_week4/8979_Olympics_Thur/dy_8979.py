n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]


#메달 개수를 기준으로 정렬(내림차순 정렬, 금메달, 은메달, 동메달 순으로 내림차순 정렮)
lst = sorted(lst, key=lambda x:(x[1], x[2], x[3]), reverse=True)

#순서대로 정렬했으니 일단 순서대로 순위 배정 후 순위 열 추가
#lst[i][4] = i+1은 안된다.
for i in range(n):
    lst[i].append(i+1)

#모두 동일한 메달 개수일때 동일한 순위를 배정한다.
for i in range(n-1):
    if lst[i][1] == lst[i+1][1]:
        if lst[i][2] == lst[i + 1][2]:
            if lst[i][3] == lst[i + 1][3]:
                lst[i+1][4] = lst[i][4]

#국가번호가 k인 인덱스 찾아서 순위 출력
for j in range(n):
    if lst[j][0] == k:
        print(lst[j][4])

# 리스트 확인
# for l in lst:
#     print(*l)



