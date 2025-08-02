# 나머지
'''
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
=> 5 8 4

첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
'''
# A, B, C = map(int,input().split())

# print((A + B) % C)
# print(((A % C) + (B % C)) % C)
# print((A * B) % C)
# print(((A % C) * (B % C)) % C)

# (2 ≤ A, B, C ≤ 10000) 체크해보기
def check_remain(get_number):
    A, B, C = get_number

    def check_size():
        for number in (A, B, C):
            if number < 2 or number > 10000:
                # print(number)
                return print('숫자의 범위는 (2 ≤ A, B, C ≤ 10000) 입니다.')

        return number_calculation()

    def number_calculation():
        print((A + B) % C)
        print(((A % C) + (B % C)) % C)
        print((A * B) % C)
        print(((A % C) * (B % C)) % C)

    check_size()

# A, B, C = map(int,input().split())
check_remain(map(int,input().split()))