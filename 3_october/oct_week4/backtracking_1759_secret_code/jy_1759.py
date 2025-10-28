from itertools import combinations

L, C = map(int, input().split())
# sorted를 하면 사전순으로 정렬됨
chars = sorted(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']

# 주어진 문자들 중 L개로 만들 수 있는 조합들
for order in combinations(chars, L):
    vowel_count = 0

    # order(현재 단어 조합)의 철자를 하나씩 보며 모음이면 vowel_count + 1
    for char in order:
        vowel_count += 1 if char in vowels else 0
    # 자음 = 전체 철자 개수 - 모음 개수
    consonant_count = L - vowel_count
    # 조건에 만족한다면 출력
    if vowel_count >= 1 and consonant_count >= 2:
        print(*order, sep = '')