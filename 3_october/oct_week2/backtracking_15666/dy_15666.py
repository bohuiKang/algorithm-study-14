n, m = map(int, input().split())
lst = list(map(int, input().split()))
# 정렬
lst.sort()
# 중복 방지
result = set()
path = [0] * m


def recur(cnt):
    if cnt == m:
        # 중복방지를 위해 set에 튜플로 변환하여 추가
        result.add(tuple(path))
        return

    # 모르겟다
    for i in range(n):
        # 오름차순 정렬
        if cnt > 0 and lst[i] < path[cnt - 1]:
            continue
        path[cnt] = lst[i]
        recur(cnt + 1)


recur(0)
result = list(result)
result.sort()

for r in result:
    print(*r)
