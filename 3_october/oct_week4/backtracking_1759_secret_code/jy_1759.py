from itertools import combinations

L, C = map(int, input().split())
# sorted를 하면 사전순으로 정렬됨
chars = sorted(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']

for order in combinations(chars, L):
    vowel_count = 0
    for char in order:
        vowel_count += 1 if char in vowels else 0
    consonant_count = L - vowel_count
    if vowel_count >= 1 and consonant_count >= 2:
        print(*order, sep = '')