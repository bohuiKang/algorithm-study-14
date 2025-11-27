#사진틀 수
N = int(input())
#전체 추천 횟수
rec_n = int(input())
#추천 받은 학생 입력값
rec_result = list(map(int, input().split()))

#사진틀 리스트, 0이면 비어있는 사진틀
picture_lst = [0]*N
#학생 추천받은 횟수 리스트 (카운팅배열, 인덱스 = 학생번호)
#0으로 초기화시 min함수 사용할때 집계되어버려서 최대값(1000)을 넘긴 값으로 초기화
rec_lst = [1001]*101

for i in range(rec_n):
    #현재 사진틀에 해당 학생이 있는 경우
    if rec_result[i] in picture_lst:
        #추천 횟수 갱신
        rec_lst[rec_result[i]] += 1

    #현재 사진틀에 해당 학생이 없고, 비어있는 사진틀이 있는 경우
    elif 0 in picture_lst:
        #추천받은 횟수 갱신
        rec_lst[rec_result[i]] = 1
        #빈 사진틀에 추가, 가장 먼저 발견한 빈 사진틀에 추가
        picture_lst[picture_lst.index(0)] = rec_result[i]

    #현재     ~                , 비어 있는 사진틀이 없는 경우
    else:
        #추천수가 가장 적고, 오래된 사진 삭제 후 새로운 학생 사진 게시
        #추천 수가 가장 적은 학생 찾기, (0으로 하면 min으로 잡혀버림)
        min_rec_num = min(rec_lst)
        # 가장 먼저 발견되는 추천수가 적은 학생을 내리고 새로운 학생 사진 게시
        for j in range(N):
            if rec_lst[picture_lst[j]] == min_rec_num:
                # 삭제되는 학생, 게시되는 학생의 추천수 초기화
                rec_lst[picture_lst[j]] = 1001
                rec_lst[rec_result[i]] = 1
                #해당 인덱스 삭제 후 게시
                picture_lst.pop(j)
                picture_lst.append(rec_result[i])
                break

#모든 추천이 끝난 후 학생 번호 순대로 정렬, 0이면 빈 사진틀이므로 삭제
for pic in picture_lst:
    if pic == 0:
        picture_lst.remove(0)
picture_lst.sort()
print(*picture_lst)