def lotto(start, cnt, path):
    if cnt > 6:  # 로또 숫자는 6자리
        return

    if cnt == 6:
        check = tuple(path)
        if check not in lottos:
            lottos.add(check)
            print(*check)
        return

    for i in range(start, len(arr)):
        lotto(i + 1, cnt + 1, path + [arr[i]])


while True:
    arr = list(map(int, input().split()))
    k = arr.pop(0)
    if k == 0:
        break
    lottos = set()
    lotto(0, 0, [])  # 시작, 개수, 내용
    print()
