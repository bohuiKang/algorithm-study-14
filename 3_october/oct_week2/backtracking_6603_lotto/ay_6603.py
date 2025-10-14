import sys
sys.stdin = open("6603_input.txt", "r")


def rec(cnt, idx, path):
    if cnt == 6:
        print(*path)
        return

    for i in range(idx, k):
        # if k - i < 6 - (cnt+1):
        #     break
        rec(cnt+1, i+1, path+[nums[i]])



while True:
    nums = list(map(int, input().split()))
    k = nums[0]

    if k == 0:
        break

    nums.pop(0) # 숫자 오름차순 정렬 위해 k 빼줌
    nums.sort()

    rec(0, 0, [])
    print()


