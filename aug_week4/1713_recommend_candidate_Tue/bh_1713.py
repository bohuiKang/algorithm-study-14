# 후보 추천하기
'''
월드초등학교 학생회장 후보는 일정 기간 동안 전체 학생의 추천에 의하여 정해진 수만큼 선정된다. 
그래서 학교 홈페이지에 추천받은 학생의 사진을 게시할 수 있는 사진틀을 후보의 수만큼 만들었다. 
추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙은 다음과 같다.

1. 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
3. 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 
그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 
이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
5. 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 
최종 후보가 누구인지 결정하는 프로그램을 작성하시오.

입력: 첫째 줄에는 사진틀의 개수 N이 주어진다. 
(1 ≤ N ≤ 20) 둘째 줄에는 전체 학생의 총 추천 횟수가 주어지고, 
셋째 줄에는 추천받은 학생을 나타내는 번호가 빈 칸을 사이에 두고 추천받은 순서대로 주어진다. 
총 추천 횟수는 1,000번 이하이며 학생을 나타내는 번호는 1부터 100까지의 자연수이다.
3
9
2 1 4 3 5 6 2 7 2

출력: 사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력한다.
2 6 7

'''
N = int(input()) # 사진틀의 개수 N
S = int(input()) # 총 추천 횟수 = 추천한 학생의 수
recommends = list(map(int, input().split())) # 추천받은 학생 번호 목록
candidates = [0] * 101 # 추천받은 횟수를 기록할 리스트, 0번 인덱스는 사용안함

pictures = [recommends[0]] # 후보자 사진틀, 첫번째 후보 미리 넣어놓기
candidates[recommends[0]] += 1 # 첫번째 후보의 추천 횟수도 미리 누적
front = rear = 0

for r in range(1, S):
    if recommends[r] in pictures: # 추천받는자가 이미 후보자 사진틀에 등록되어 있음
        candidates[recommends[r]] += 1 
        continue
    if len(pictures) != N: # 후보자 사진틀에 자리가 있으면
        pictures.append(recommends[r])
        candidates[recommends[r]] += 1 # 추천 적립
    elif len(pictures) == N: # 사진틀이 꽉차면
        min = 0
        for i in range(1, N):
            if candidates[pictures[min]] > candidates[pictures[i]]: # 추천수가 제일 작은 후보자 찾기 or 추천수 동일할때 제일 먼저 등록된 후보자 찾기
                min = i
        candidates[pictures[min]] = 0 # 추천수 0로
        pictures.pop(min) # 탈락
        # 사진틀에 자리남
        pictures.append(recommends[r])
        candidates[recommends[r]] += 1 # 추천 적립

pictures.sort()
for p in pictures:
    print(p, end=' ')