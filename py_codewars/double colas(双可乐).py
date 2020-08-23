def who_is_next(names, r):
    i = len(names)
    count = 0
    while count <= r:
        count += i
        i *= 2
    n = r - (count - i//2)
    save_num = n // (i//2//len(names))
    if n % (i//2//len(names)) == 0:
        return names[save_num -1]
    else:
        return names[save_num]
names = ["Sheldon", "Leonard","Penny", "Rajesh", "Howard"]
print(who_is_next(names,100))
































