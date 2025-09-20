# 비내림차순: 항상 왼쪽원소 <= 오른쪽원소 여야 함
# 1부터 N까지 자연수 중 M개를 골라서 비내림차순인 수열을 한줄씩 모두 출력
# 같은 수를 여러번 골라도 된다
N, M = map(int, input().split())
def recur(depth, path):
    for i in range(depth - 1):  # 가지치기: 내림차순이 되면 즉시 종료
        if path[i] > path[i + 1]:
            return
    if depth == M:  # 기저조건: M개의 숫자를 모두 고르면 종료
        print(*path)
        return
    for i in range(1, N+1): # 1 ~ N 까지의 수 중에서 1개 골라서 수열에 추가
        recur(depth + 1, path + [i])
recur(0, [])