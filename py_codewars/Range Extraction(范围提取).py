def solution(l):
    new_list = []
    i , j = 0 , 1
    while j <= len(l):
        try:
            if l[j-1] + 1 != l[j]:
                if len(l[i:j]) > 2:
                    new_list.append(str(l[i]) + '-' + str(l[j-1]))
                    i = j
                    j += 1
                else:
                    for s in l[i:j]:
                        new_list.append(str(s))
                    i = j
                    j += 1
            elif l[j-1] + 1 == l[j]:
                j += 1
        except:
            if len(l[i:j]) > 2:
                new_list.append(str(l[i]) + '-' + str(l[j - 1]))
                j += 1
            else:
                for s in l[i:j]:
                    new_list.append(str(s))
                j += 1
    return ','.join(new_list)
print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))