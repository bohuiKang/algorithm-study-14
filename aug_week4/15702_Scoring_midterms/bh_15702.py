# 중간고사 채점
'''
입력:
4 4
10 20 30 40
1 O X X X
2 X O X X
3 X X O X
4 X X X O

4 8
10 20 30 40
1 O X X X
2 X O X X
3 X X O X
4 X X X O
80 O O O O
70 O O O O
60 O O O O
50 O O O O

출력:
4 40

50 100
'''
# 문제 N개, 응시자 M명
N, M = map(int, input().split())
scores = [0] + list(map(int, input().split())) # 0번 사용 안함
students = [list(input().split()) for _ in range(M)]

results = [0] * M
for i in range(M):
    for j in range(1, N+1):
        if students[i][j] == 'O': # 정답이면
            results[i] += scores[j]

max_score = 0
for i in range(1, M):
    if results[max_score] < results[i]:
        max_score = i
    elif results[max_score] == results[i]:
        if int(students[max_score][0]) > int(students[i][0]):
            max_score = i

print(f'{students[max_score][0]} {results[max_score]}')




