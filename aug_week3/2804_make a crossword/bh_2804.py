# 크로스워드 만들기
'''
창영이는 크로스워드 퍼즐을 만들려고 한다.

두 단어 A와 B가 주어진다. A는 가로로 놓여야 하고, B는 세로로 놓여야 한다. 
또, 두 단어는 서로 교차해야 한다. (정확히 한 글자를 공유해야 한다) 
공유하는 글자는 A와 B에 동시에 포함되어 있는 글자여야 하고, 그런 글자가 여럿인 경우 A에서 제일 먼저 등장하는 글자를 선택한다. 
마찬가지로 이 글자가 B에서도 여러 번 등장하면 B에서 제일 처음 나오는 것을 선택한다. 
예를 들어, A = "ABBA"이고, B = "CCBB"라면, 아래와 같이 만들 수 있다.
.C..
.C..
ABBA
.B..

입력: 첫째 줄에 두 단어 A와 B가 주어진다. 두 단어는 30글자 이내이고, 공백으로 구분되어져 있다. 
또, 대문자로만 이루어져 있고, 적어도 한 글자는 두 단어에 포함되어 있다.
BANANA PIDZAMA

출력: A의 길이를 N, B의 길이를 M이라고 했을 때, 출력은 총 M줄이고, 각 줄에는 N개 문자가 있어야 한다. 
문제 설명에 나온 것 같이 두 단어가 교차된 형태로 출력되어야 한다. 나머지 글자는 '.'로 출력한다.
.P....
.I....
.D....
.Z....
BANANA
.M....
.A....

'''
# A: 가로 글자, B: 세로 글자
A, B = input().split()

cross_word = [['.']*len(A) for _ in range(len(B))]

# 같은 글자의 위치 값 저장
aa = 0
bb = 0
same_find = 0
### A를 기준으로 같은 글자를 찾아야 한다고 함. 문제의 어디에서 A를 우선해야한다고 ...
### 설마 이 문구인가? 'A에서 제일 먼저 등장하는 글자를 선택한다.' :)...
# for i in range(len(B)):
#     for j in range(len(A)):
#         if B[i] == A[j]:
#             bb = i
#             aa = j
#             same_find = 1
#             break
#     if same_find != 0: # 안쪽 for문에서 같은 글자 위치 값이 할당되었으면, 바깥 for문도 break
#         break

for j in range(len(A)):
    for i in range(len(B)):
        if A[j] == B[i]:
            bb = i
            aa = j
            same_find = 1
            break
    if same_find != 0: # 안쪽 for문에서 같은 글자 위치 값이 할당되었으면, 바깥 for문도 break
        break

# print('bb:', bb)
# print('aa:', aa)

for i in range(len(B)):
    cross_word[i][aa] = B[i]

for j in range(len(A)):
    cross_word[bb][j] = A[j]
            
for row in cross_word: # 띄어쓰기 없는 출력
    print(''.join(row))
