# 시험 성적
'''
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 
70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성
입력: 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수
100
출력:
A
'''
T = int(input())

def grade(T):
    if 90 <= T <= 100:
        return 'A'
    elif T >= 80:
        return 'B'
    elif T >= 70:
        return 'C'
    elif T >= 60:
        return 'D'
    else:
        return 'F'

print(grade(T))