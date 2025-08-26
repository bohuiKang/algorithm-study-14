N, M = map(int, input().split())
score = list(map(int, input().split()))
students_score = [list(input().split()) for _ in range(M)]
result_score = []

for i in range(M):
    s_sum = 0
    for k in range(N):
        if students_score[i][k+1] == "O":
            s_sum += score[k]
    result_score.append([int(students_score[i][0]), s_sum]) #int 안하면 틀림 치사한놈

result_score.sort(key=lambda x: (-x[1], x[0]))
print(*result_score[0])