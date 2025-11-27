# 문자의 길이 l, 알파벳 수 c
l, c = map(int, input().split())
# 알파벳 리스트
lst = list(input().split())
# 증가하는 순서로 정렬
lst.sort()

# 문자열
path = [0]*l
# 중복 방지 리스트
used = [False]*c

# 모음의 수를 반환하는 함수, 자음의 개수 = 글자 수 - 모음
def check_vo(string):
    # 모음
    vo = 0
    for s in string:
        if s in ['a', 'e', 'i', 'o', 'u']:
            vo += 1
    return vo

def recur(cnt, prev):
    if cnt == l:
        # 문자열에 최소 모음 1개, 자음 2개 있는지 확인
        check = check_vo(path)
        if check >= 1 and l-check >= 2:
            print(*path, sep='')
        return

    for i in range(c):
        # 사용한 적 있다면 건너뛰기
        if used[i]:
            continue

        # 직전 알파벳보다 작다면 건너뛰기
        if prev > lst[i]:
            continue

        #중복표시
        used[i] = True
        path[cnt] = lst[i]
        recur(cnt + 1, lst[i])
        used[i] = False

# 문자열에 최소 모음 1개, 자음 2개 있는지 확인
check = check_vo(lst)
if check >= 1 and c-check >= 2:
    # 대문자가 소문자보다 작다
    recur(0, 'A')




