word = input()

left_len = len(word) % 10 # 마지막 글자 개수
num_for = len(word) // 10 # 반복 횟수

for i in range(num_for):
    print(word[10*i:10*(i+1)])

if left_len > 0:
    print(word[10*num_for:10*num_for+left_len])

