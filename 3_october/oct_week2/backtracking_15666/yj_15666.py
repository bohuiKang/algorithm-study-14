# 백트래킹을 이용한 비내림차순 중복 조합 생성
def backtracking(start):
    # 기저조건: 수열의 길이가 m이 되면 출력
    if len(result) == m:
        print(*result)
        return
    
    # start 인덱스부터 끝까지 탐색 (비내림차순 유지)
    for i in range(start, len(numbers)):
        result.append(numbers[i])
        backtracking(i)  # 같은 인덱스부터 시작 (중복 허용)
        result.pop()

n, m = map(int, input().split())  # n: 수의 개수, m: 수열의 길이

# 주어진 n개의 수 입력
numbers = list(map(int, input().split()))

# 중복 제거를 위해 set으로 변환 후 정렬
numbers = sorted(set(numbers))

# 결과를 저장할 리스트
result = []


# 백트래킹 시작 (인덱스 0부터)
backtracking(0)