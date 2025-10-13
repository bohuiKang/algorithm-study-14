N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []  # 이미 출력된 같은 수열 있는지 확인하기 위한 리스트
path_first = [0] * M
idxs_first = [-1] * M

