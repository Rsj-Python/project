def perimeter(n):
    new_list = [1,1]
    for i in range(n-1):
        new_list.append(new_list[i] + new_list[i+1])
    return sum(new_list) * 4
print(perimeter(1))