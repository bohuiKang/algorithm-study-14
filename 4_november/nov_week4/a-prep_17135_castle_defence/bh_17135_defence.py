from itertools import combinations

def defence(arrows):
    global max_kill

    catch = set()

    for line in range(n, -1, -1): # 적의 위치가 아닌 궁수의 위치를 이동 시킴
        temp_catch = set()
        for arrow in arrows: # 궁수의 위치 (열번호)
            distances = []
            for enemy in enemies: # 적들의 위치를 전부 비교
                if enemy in catch: # 이미 잡은 적군이면 pass
                    continue
                x, y = enemy
                if x < line: # 지나가지 않은 적군
                    distance = abs(line - x)+abs(arrow - y)
                    if distance <= d: # 적군의 위치가 잡을 수 있는 위치에 있다면 리스트에 추가
                        distances.append((distance, y, x)) # 열 번호가 그 다음 정렬 기준이 되도록

            if len(distances): # 죽일 수 있는 적이 있으면
                distances.sort() # 정렬
                temp_catch.add((distances[0][2], distances[0][1]))

        catch.update(temp_catch)

    return len(catch)


n, m, d = map(int, input().split()) # n*m 크기의 에서 적이 몰려오고, 궁수는 d 거리 안의 적을 맞출 수 있다.
enemy_pos = [list(map(int, input().split())) for _ in range(n)] # 적들의 위치 => 1
castle = [i for i in range(m)] # 성의 크기
bows = list(combinations(castle, 3)) # 성에 배치할 궁수들의 위치 조합

max_kill = -1

enemies = set()
for r in range(n):
    for c in range(m):
        if enemy_pos[r][c] == 1:
            enemies.add((r, c))

for bow in bows:
    max_kill = max(max_kill, defence(bow))

print(max_kill)