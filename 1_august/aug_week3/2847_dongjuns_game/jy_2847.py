n = int(input())
scores = []
scores_goal = []
adj_sum = 0

for i in range(1, n + 1):
    scores.append(int(input()))

count = 0

for j in range(n-1, 0, -1):
    while scores[j] <= scores[j-1]:
        scores[j-1] -= 1
        count += 1

print(count)