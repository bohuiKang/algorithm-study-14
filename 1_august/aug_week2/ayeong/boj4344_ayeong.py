C = int(input())

for tc in range(C):
    N_grade = list(map(int, input().split())) # 학생수, 학생점수 리스트 0인덱스는 무조건 학생수

    N = N_grade[0] # 학생수
    sum_grade = 0
    for i in range(1,N+1): # 전체 점수합 구하기
        sum_grade += N_grade[i]

    avg = sum_grade / N # 평균 구하기

    cnt = 0
    for i in range(1,N+1): # 퍼센트 구하기 위한 평균 이상 점수 수 구하기
        if avg < N_grade[i]:
            cnt += 1

    per_score = cnt / N * 100 # 평균 이상 점수 퍼센트

    print(f'{per_score: .3f}%')