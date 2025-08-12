H, M =map(int, input().split())

nM = M -45
nH = H
if nM < 0:
    nH = H -1
    nM = 60+nM

if nH < 0:
    nH =23

print(nH, nM)