#백트래킹을 이용한 조합 생성
def backtracking(cnt, start):
    # 기저조건: 6개를 모두 선택했으면 출력
    if cnt == 6:
        print(*result)
        return
    
    # start 인덱스부터 끝까지 탐색
    for i in range(start, len(s)):
        result.append(s[i])  # 현재 수를 선택
        backtracking(cnt + 1, i + 1)  # 다음 인덱스부터 탐색
        result.pop()

while True:
    # 입력 받기
    data = list(map(int, input().split()))
    k = data[0]  # 집합 S의 크기
    
    # k가 0이면 종료
    if k == 0:
        break
    
    s = data[1:]  # 집합 S의 원소들
    result = []  # 선택된 수들을 저장할 리스트
    
    backtracking(0, 0)
    print()