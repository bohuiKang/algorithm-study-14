from collections import deque, defaultdict

# 모두가 친구가 되었는지 확인하는 함수
def is_all(lst):
    for a in range(1, n+1):
        # 친구 아닌 사람이 있다면 false 반환
        if lst[a]:
            return False
    return True

n = int(input())
# 친구 관계 딕셔너리
# lst = [[0] for _ in range(n+1)]
dic = defaultdict(list)

while True:
    x, y = map(int, input().split())
    # 회원번호는 1부터 시작, -1이라면 종료
    if x == -1:
        break
    dic[x].append(y)
    dic[y].append(x)
    # lst[x].append(y)
    # lst[y].append(x)

# 회장 후보 점수
min_n = float('inf')
# 회장 후보 리스트
can_lst = []
for i in range(1, n+1):
    # 친구 목록(= 방문 목록)
    friend = [True]*(n+1)
    # 방문 예정 목록 큐
    q = deque()
    # 큐에 본인, 횟수 삽입
    q.append((i, 0))
    # 친구 표시
    friend[i] = False

    while q:
        now, num = q.popleft()
        # 가지치기, 회장 후보 점수보다 크다면 진행할 필요 없음
        if num >= min_n:
            break
        for f in dic[now]:
            #아직 친구가 아니라면
            if friend[f]:
                q.append((f, num+1))
                # 친구 표시
                friend[f] = False
        # 모두와 친구가 되었는지 확인
        if is_all(friend):
            # 모두와 친구가 되었다면
            # 친구 표시를 q를 실행하기 전에 했으니 += 1
            num += 1
            if min_n > num:
                min_n = num
                can_lst = [i]
            else:
                can_lst.append(i)
            break

print(f'{min_n} {len(can_lst)}')
print(*can_lst)