# 자음 2개이상, 모음 1개이상
# 낱말들을 리스트로 입력받음
# 재귀를 통해 단어의 길이를 기저조건으로 조합하고 result 리스트에 append
# 마지막에 result를 sort해서 출력
L, C = map(int, input().split())
letters = sorted(input().split())  # 사전순 정렬

vowels = {'a', 'e', 'i', 'o', 'u'}
result = []

def dfs(start, path):
    # 기저조건: 길이가 L인 조합 완성
    if len(path) == L:
        v_cnt = sum(1 for ch in path if ch in vowels)
        c_cnt = L - v_cnt
        if v_cnt >= 1 and c_cnt >= 2:
            result.append(''.join(path))
        return

    # 다음 문자 선택
    for i in range(start, C):
        dfs(i + 1, path + [letters[i]])

dfs(0, [])

for word in result:
    print(word)