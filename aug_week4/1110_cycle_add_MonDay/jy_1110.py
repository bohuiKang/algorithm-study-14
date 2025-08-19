def make_1(start, end):
    global cnt, a
    new_end = str((int(start) + int(end)) % 10)
    new_start = end
    new_number = new_start + new_end
    cnt += 1

    if new_number == a:   # 전역 a와 비교
        return cnt
    else:
        return make_1(new_start, new_end)

a = input().strip()
if len(a) == 1:
    a = "0" + a

cnt = 0
print(make_1(a[0], a[1]))
