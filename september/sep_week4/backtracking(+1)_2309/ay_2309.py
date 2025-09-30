dwarfs = [0]*9
for i in range(9): # 난쟁이 입력 받기
    dwarfs[i] = int(input())

dwarfs.sort()

def backtrack(sum_tall, cnt, real_7, idx):
    if cnt == 7: # 7명 고르면 끝내기
        if sum_tall == 100: # 7명 골랐을 때 100이면 끝내고 해당 7명을 return 함
            return real_7
        return []

    ans =[]

    for i in range(idx, 9):
        ans += backtrack(sum_tall+dwarfs[i], cnt+1, real_7+[dwarfs[i]], i+1) # return 값을 다 더하는데 real_7을 찾았으면
        if ans: # 7난장이 찾았으면 ans = true 라서 끝나도록
            return ans

    return []


result = backtrack(0, 0, [], 0)
for dwarf in result:
    print(dwarf)
