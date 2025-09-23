N = int(input())
nums = list(map(int, input().split()))
plus, minus, times, div = map(int, input().split())

def recur(plus, minus, times, div, cnt, total):
    global min_result
    global max_result

    if cnt == N:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return

    if plus > 0:
        recur(plus-1, minus, times, div, cnt+1, total+nums[cnt])

    if minus > 0:
        recur(plus, minus-1, times, div, cnt+1, total-nums[cnt])

    if times > 0:
        recur(plus, minus, times-1, div, cnt+1, total*nums[cnt])

    if div > 0:
        recur(plus, minus, times, div-1, cnt+1, int(total/nums[cnt]))

min_result=float("inf")
max_result=-float("inf")
recur(plus, minus, times, div, 1, nums[0])

print(max_result)
print(min_result)



