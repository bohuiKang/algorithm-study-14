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

#왜 틀렸는지 모르겠어염

# n = int(input())
# scores = []
# scores_goal = []
# adj_sum = 0
#
# for i in range(1, n + 1):
#     scores.append(int(input()))
# scores = scores[::-1]
#
# for j in range(0, n):
#     scores_goal.append(scores[-1] - j * 1)
#
# for k in range(n):
#     if scores[k] != scores_goal[k]:
#         adj = scores[k] - scores_goal[k]
#         adj_sum += adj
#
# print(adj_sum)