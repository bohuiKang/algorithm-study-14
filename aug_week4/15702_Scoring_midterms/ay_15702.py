N, M = map(int, input().split())
score = [0] + list(map(int, input().split()))
student = [list(input().split()) for _ in range(M)]

max_val = -1
prize_stu = 100000
for i in range(M):
    sum = 0
    for num in range(1, N+1): # 1~N 번 문제까지
        if student[i][num] == 'O': # 맞으면
            sum += score[num] # 점수 더하기
    if sum > max_val: # MAX 값 갱신
        max_val = sum
        prize_stu = int(student[i][0]) # MAX 값 인 수험번호
    elif sum == max_val:
        if prize_stu > int(student[i][0]):
            prize_stu = int(student[i][0])

print(prize_stu, max_val)