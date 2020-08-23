def odd_one_out(s):
    new = list(s)
    new_list = []
    for i in new:
        if new.count(i) % 2 != 0 and i not in new_list:
            new_list.append(i)
    return new_list
print(odd_one_out('Hello World'))