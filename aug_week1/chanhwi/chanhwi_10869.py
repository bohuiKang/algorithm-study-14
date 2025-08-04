# 사칙연산
'''
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

입력: 
7 3 

출력: 
10
4
21
2
1
'''
A, B = list(map(int, input().split()))
a = A + B
b = A - B
c = A * B
d = A // B
e = A % B
print(f'{a}\n{b}\n{c}\n{d}\n{e}')