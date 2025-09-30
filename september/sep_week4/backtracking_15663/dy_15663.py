'''
n, m = map(int, input().split())
path = [0] * m

lst = list(map(int, input().split()))
# 비내림차순을 위해 정렬
lst.sort()

# 중복 체크
used = [0] * n

#직전 값
prev = 10001

def recur(cnt):
    global prev
    if cnt == m:
        print(*path)
        return

    for i in range(n):
        if not used[i] and lst[i] != prev:
            path[cnt] = lst[i]
            used[i] = 1
            recur(cnt + 1)
            used[i] = 0
            prev = lst[i]


recur(0)
'''
n, m = map(int, input().split())
path = [0] * m

lst = list(map(int, input().split()))
# 비내림차순을 위해 정렬
lst.sort()

# 중복 체크
used = [0] * n

result = set()


def recur(cnt):
    if cnt == m:
        # set에는 리스트를 추가할 수 없음
        # tuple로 변경하여 값 추가
        result.add(tuple(path))
        return

    for i in range(n):
        if not used[i]:
            path[cnt] = lst[i]
            used[i] = 1
            recur(cnt + 1)
            used[i] = 0


recur(0)

# set에는 순서가 없지만 sorted는 된다
# 정렬된 리스트가 반환
result = sorted(result)
for r in result:
    print(*r)