def recur(start, path):

    if len(path) == L:
        vowel = 0
        for a in 'aeiou': # 모음은 1개 이상
            if a in path:
                vowel += 1
        if vowel >= 1 and (L - vowel) >= 2: # 자음은 2개 이상
            print(''.join(path))

    for i in range(start, C):
        recur(i+1, path + [alpha[i]])


L, C = map(int, input().split()) # L개의 암호문, C개의 문자
alpha = sorted(list(input().split())) # C개의 알파벳 소문자

recur(0, [])

