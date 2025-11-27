def main():
    def recur(start, path):
        if len(path) == 6:
            print(*path)
            return
        for i in range(start, k):
            recur(i + 1, path + [S[i]])

    while True:
        S = list(map(int, input().split()))     # S: 숫자들 집합(오름차순)
        k = S.pop(0)
        if k == 0:
            return
        recur(0, [])
        print()

main()