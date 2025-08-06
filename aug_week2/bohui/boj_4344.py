# 평균은 넘겠지
'''
입력: 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

출력: 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 
정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.
40.000%
57.143%
33.333%
66.667%
55.556%
'''
T = int(input())

for tc in range(T):
    N, *n_scores = list(map(int, input().split()))

    score_sum = 0
    for score in n_scores:
        score_sum += score

    score_average = score_sum / N
    above_average = 0
    for score in n_scores:
        if score_average < score:
            above_average += 1
    
    # 소수점 세자리까지 표시 및 반올림 작업
    above_rate_calculate = int(above_average/N * 1e6)
    if above_rate_calculate % 10 >= 5: # 1의 자리수가 5 이상일 때,
        # 10의 자리 하나 올리고, 1의 자리 수 제거 후 / 1000으로 소수점 표시
        above_rate = (above_rate_calculate + 10 - above_rate_calculate % 10) / 10000
    else:
        above_rate = (above_rate_calculate - above_rate_calculate % 10) / 10000 
    
    print(f'{above_rate}%')