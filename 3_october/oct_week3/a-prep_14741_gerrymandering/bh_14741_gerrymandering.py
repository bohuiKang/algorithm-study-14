from collections import deque

def com(start, path_A, path_B, population):
    global less_gap

    if start == N:
        if not path_A or not path_B:
            return

        # 인접한 구역인지 확인하기
        if not check_adj(path_A) or not check_adj(path_B):
            return  # 인접한 구역이 아님

        # 위 코드를 통과하면 2구역 안의 선거구가 모두 인접한 구역임
        less_gap = min(less_gap, abs(population - (total_people - population)))
        return

    # 구역 나누기
    # for area in range(start, N): => for 문 사용 안해도 됨
    com(start+1, path_A+[start], path_B, population+people[start]) # 포함
    com(start+1, path_A, path_B+[start], population) # 포함안함


def check_adj(path): # 인접한 구역인지 확인하기
    q = deque([path[0]])
    visited = {path[0]} # set

    while q:
        s = q.popleft()
        for nxt_area in adj_area[s][1:]:
            nxt = nxt_area - 1
            if nxt in path:
                if nxt not in visited:
                    # 지나가지 않은 구역이라면
                    visited.add(nxt)
                    q.append(nxt)

    return len(visited) == len(path)


N = int(input()) # N개의 구역
people = list(map(int, input().split())) # 구역별 인구수
adj_area = [list(map(int, input().split())) for _ in range(N)] # 인접 지역

total_people = sum(people)
less_gap = float('inf')

com(0, [], [], 0)

if less_gap == float('inf'):
    print(-1)
else:
    print(less_gap)

# 아래는 gemini의 수정 답
'''
from collections import deque
import sys

# 입력이 많을 수 있으므로 재귀 깊이를 설정
# sys.setrecursionlimit(10**6) 

# N개의 구역, 인구수 배열 people, 인접 정보 adj_area (adjacency list)
N = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
adj_area = []
for _ in range(N):
    # 입력 형태: [인접 구역 수, 인접 구역 1, 인접 구역 2, ...]
    adj_area.append(list(map(int, sys.stdin.readline().split()))[1:]) # 첫 번째 숫자는 제외하고 인접 구역 번호만 저장

# 결과 변수 초기화
min_diff = float('inf')
total_people = sum(people)

# -----------------------------------------------------
# 1. 연결성 검사 함수 (BFS 사용)
# path: 검사할 선거구에 포함된 구역 번호 리스트 (0-based index)
# -----------------------------------------------------
def is_connected(path):
    if not path:
        return False # 구역이 하나도 없으면 연결될 수 없음

    start_node = path[0]
    
    # 방문 여부 배열 초기화 (전체 N개 구역에 대해)
    visited = {node: False for node in path}
    
    q = deque([start_node])
    visited[start_node] = True
    count = 1 # 탐색된 구역 수

    while q:
        curr = q.popleft()
        
        # curr 구역과 인접한 모든 구역을 확인
        # adj_area에는 1-based index로 저장되어 있으므로 -1을 해줘야 함
        for neighbor in adj_area[curr]:
            neighbor_idx = neighbor - 1

            # 1. 인접 구역이 현재 선거구(path)에 포함되어 있고
            # 2. 아직 방문하지 않았다면
            if neighbor_idx in path and not visited[neighbor_idx]:
                visited[neighbor_idx] = True
                q.append(neighbor_idx)
                count += 1
    
    # BFS로 탐색된 구역 수가 선거구의 전체 구역 수와 같으면 연결됨
    return count == len(path)


# -----------------------------------------------------
# 2. 모든 부분집합 생성 함수 (DFS/재귀)
# A_subset: 선거구 A에 포함된 구역 번호 리스트 (0-based index)
# -----------------------------------------------------
def find_subsets(idx, A_subset):
    global min_diff

    # Base Case: 모든 구역(N개)에 대해 선택을 완료했을 때
    if idx == N:
        # 두 선거구 A와 B를 결정
        A = A_subset
        B = [i for i in range(N) if i not in A] # 전체 구역 중 A에 없는 구역이 B

        # 1. 각 선거구가 최소 1개 이상의 구역을 포함하는지 확인
        if 0 < len(A) < N:
            
            # 2. 두 선거구 A와 B 각각이 연결되어 있는지 확인
            if is_connected(A) and is_connected(B):
                
                # 3. 유효한 분할이므로 인구 차이 계산 및 갱신
                pop_A = sum(people[i] for i in A)
                # pop_B = total_people - pop_A 
                
                # 인구 차이 계산 (pop_A - pop_B 의 절대값)
                diff = abs(pop_A - (total_people - pop_A))
                min_diff = min(min_diff, diff)
        
        return

    # 재귀 호출 1: 현재 idx 구역을 선거구 A에 포함 (선택)
    find_subsets(idx + 1, A_subset + [idx])
    
    # 재귀 호출 2: 현재 idx 구역을 선거구 B에 포함 (선택 안 함)
    find_subsets(idx + 1, A_subset)


# -----------------------------------------------------
# 3. 메인 로직 실행
# -----------------------------------------------------

# DFS 시작 (idx 0부터, A_subset은 빈 리스트에서 시작)
find_subsets(0, [])

# 결과 출력
if min_diff == float('inf'):
    print(-1) # 가능한 분할이 없었음
else:
    print(min_diff)

'''