from collections import deque

def check_friends(friends_list):
    q = deque()
    for friend in friends_list:
        q.append((friend, 2)) # 친구 q에 추가
        friends[friend] = 1 # 친구들은 미리 채우기

    while q:
        member, point = q.popleft()
        ans = point
        f_lst: list = arr[member] # 회원의 친구의 친구... 추가
        for second in f_lst:
            if friends[second] == 0: # 확인친구가 비어있으면
                friends[second] = point
                q.append((second, point+1))


# 입력
n = int(input()) # 회원수
arr = [list() for _ in range(n+1)] # 회원의 친구 저장 리스트
points = [50] + [0 for _ in range(n)] # 0번째 인덱스 사용x + 회원 점수

while True: # 회원의 친구 저장
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n+1): # 친구 촌수? 확인
    friends = [0 for _ in range(n+1)] # 친구확인 리스트
    friends[i] = -1 # 본인의 값은 -1로 미리 저장
    check_friends(arr[i])
    points[i] = max(friends) # friends의 max 값을 points 리스트에 저장
low_point = min(points) # 최소 점수
low_person = [] # 최소 점수인 회원 저장 리스트
for check in range(1, n+1):
    if points[check] == low_point:
        low_person.append(check)

# 출력
print(low_point, len(low_person))
print(*low_person)