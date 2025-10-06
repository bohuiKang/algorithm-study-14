N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

sol_r = 0 # 열에 필요한 병사수
sol_c = M # 행에 필요한 병사수
# 행과 열 중에서 x가 없는줄을 센 다음 더 큰값이 필요한 최소 경비원 수가 된다.

for arr_r in arr: # 열 순환하며 X 없으면 필요한 병사수 +1
    if 'X' not in arr_r:
        sol_r += 1

for c in range(M):
    for r in range(N): # 행 순환하며 X면 해당열 끝까지 확인안하고 필요한 병사수 -1 (행의 경우 최대 병사수가초기값)
        if arr[r][c] == 'X':
            sol_c -= 1
            break


print(max(sol_r, sol_c))