# 백트래킹을 이용한 중복 순열 생성
def recur():
    # 기저조건: m개 뽑으면 출력
    if len(result) == m:
        print(*result)
        return
    
    # 중복을 허용하므로 매번 모든 수를 선택 가능
    for num in arr:
        result.append(num)
        recur()  # 재귀 호출
        result.pop()  # 백트래킹: 마지막 수 제거

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 중복 제거를 위해 set으로 변환 후 정렬
arr = sorted(set(arr))

# 결과를 저장할 리스트
result = []

recur()