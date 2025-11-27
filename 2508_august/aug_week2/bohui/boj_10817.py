# 세수
'''
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
입력:
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
출력:
두 번째로 큰 정수를 출력한다.
'''
int_list = list(map(int, input().split()))

for i in range(3-1, 0, -1):
    for j in range(i):
        if int_list[j] > int_list[j+1]:
            int_list[j], int_list[j+1] = int_list[j+1], int_list[j]

print(int_list[1])