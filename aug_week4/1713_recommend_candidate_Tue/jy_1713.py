photo_size = int(input())
student = int(input())

gallery = []
rec_lst = list(map(int, input().split()))
order = 0 #순서를 써줘야 함 ... 망할

for current_student in rec_lst:
    for i in range(len(gallery)):
        if current_student == gallery[i][0]:
            gallery[i][1] += 1
            break

    else:
        if len(gallery) < photo_size:
            gallery.append([current_student, 1, order])
            order += 1

        else:
            #정렬기준 -> 추천 횟수, 게시 순서
            gallery.sort(key=lambda x: (x[1], x[2]))
            gallery.pop(0)
            gallery.append([current_student, 1, order])

            order += 1

gallery.sort(key=lambda x: x[0])
print(*[x[0] for x in gallery])

# result = []
# for c in gallery:
#     result.append(c[0])
# print(*result)