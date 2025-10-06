#문제의 개수 N, 응시자의 수 M
N, M = map(int, input().split())
#문제의 번호 -1 = 인덱스
score_lst = list(map(int, input().split()))
#채점 결과 리스트, result_lst[i][0] 수험번호,
result_lst = [list(input().split()) for _ in range(M)]
#수험번호 순대로 정렬, int가 없으면 안되네..
result_lst.sort(key=lambda x:int(x[0]))

best_score = -1
best_score_student = -1
for i in range(M):
    score = 0
    for j in range(1, N+1):
        #맞았을경우
        if result_lst[i][j] == 'O':
            #score_lst[j-1] = 배점
            score += score_lst[j-1]
    #다 채점한 후 최고점과 학생번호 갱신
    if best_score < score:
        best_score = score
        best_score_student = result_lst[i][0]


#아무도 맞춘 사람이 없을때, 가장 번호가 작은 사람과 0 출력
if best_score == -1:
    print(result_lst[0][0], 0)


print(best_score_student, best_score)