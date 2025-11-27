A, B = input().split()
N = len(A)
M = len(B)
arr = [['.'] * N for _ in range(M)]

same_idx = 0 # 같은

for A_idx in range(N):
    if A[A_idx] in B : # A 문자 하나하나 돌면서 B에 있으면

        for B_idx in range(M):
            if B[B_idx] == A[A_idx]: # B문자 몇번째와 같은지 확인 후 break (제일 먼저 등장이므로 break으로 나옴)
                break

        break # 바깥 for문 나오기 위한 break

for i in range(M): # B문자 넣기
    arr[i][A_idx] = B[i]

arr[B_idx] = list(A) # A 문자는 같은 행 이라서 그냥 리스트로 통째로 넣기 가능

string_arr = []
for i in range(M):
    string_arr.append(''.join(arr[i]))

for row in string_arr:
    print(row)