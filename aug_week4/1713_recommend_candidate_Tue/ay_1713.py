'''
다시 짜야함... 예외 고려 해줘야함



'''

N = int(input()) # 사진틀 갯수 (나타내는 후보 갯수)
all_num = int(input()) # 총 추천 횟수
std_num = list(map(int, input().split()))

lst = [] # 후보 리스트 N명을 추리기 위한 lst


for idx in range(N): # N명 후보를 일단 넣음
    lst.append([std_num[idx], 1]) # [후보 번호, 추천수]

for idx in range(N, all_num): # 나머지 남은 후보 만큼 반복
    min_v = 1000 #최소 추천수 초기화
    for i in range(N):
        std, cnt = lst[i]
        if std == std_num[idx]: # 일치 후보 번호 있으면 추천수 +1
            lst[i][1] += 1
            break
        else:
            if min_v > cnt: # 없으면 제일 추천수 작은 후보 찾아서 교체 오래된 순으로 교체
                min_v = cnt
                min_idx = i
    else:
        del lst[min_idx]
        lst.append([std_num[idx], 1])



lst.sort()
for i in range(N):
    print(lst[i][0], end=' ')





