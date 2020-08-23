def find_even_index(list):
    for i in range(len(list)):
        left_sum = 0
        right_sum = 0
        if i == 0:
            for a in range(i+1,len(list)):
                right_sum += list[a]
            if right_sum == 0:
                return i
        elif i > 0 and i < len(list) - 1:
            for j in range(0, i):
                left_sum += list[j]
            for k in range(i + 1, len(list)):
                right_sum += list[k]
            if left_sum == right_sum:
                return i
        elif i == len(list) - 1:
            for b in range(0,len(list)-1):
                left_sum += list[b]
            if left_sum == 0:
                return i
    return -1
print(find_even_index([1,2,3,2,1]))








