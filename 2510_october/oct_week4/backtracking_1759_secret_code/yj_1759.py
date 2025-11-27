def recur(cnt, start, vowel_cnt, consonant_cnt):  # 암호 몇 개 뽑았는지, 어디까지 뽑았는지, 모음 카운트, 자음 카운트
    if cnt == L:
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print("".join(path))
            return
        else:
            return

    # 재귀 파트
    for i in range(start, C):
        if not visited[i]:
            path.append(alphabets[i])
            visited[i] = 1
            # 모음 뽑았으면
            if alphabets[i] in ['a', 'e', 'i', 'o', 'u']:
                recur(cnt + 1, i + 1, vowel_cnt + 1, consonant_cnt)
            # 자음 뽑았으면
            else:
                recur(cnt + 1, i + 1, vowel_cnt, consonant_cnt + 1)
            path.pop()
            visited[i] = 0

L, C = map(int, input().split())
alphabets = list(input().split())

alphabets.sort()

path = []
visited = [0] * C
recur(0, 0, 0, 0)