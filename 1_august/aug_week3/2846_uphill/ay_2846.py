N = int(input())

road = list(map(int, input().split()))

max_uphil = 0
i = 0


while i < N-1:
    S = []
    S.append(road[i])

    if road[i] >= road[i+1]:
        S.pop()
        i += 1
    else:
        while i+1 <N and road[i] < road[i+1] :
            S.append(road[i+1])
            i += 1
        uphil = S[-1] - S[0]
        if max_uphil <uphil:
            max_uphil = uphil

print(max_uphil)


