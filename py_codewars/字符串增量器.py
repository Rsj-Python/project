def increment_string(strng):
    if len(strng) == 0:
        return str(1)
    elif len(strng) == 1:
        return str(int(strng)+1)
    for i in range(-1, -len(strng) - 1, -1):
        if strng[i] != '0' and strng[i] != '1'and strng[i] != '2'and strng[i] != '3'and strng[i] != '4'and strng[i] != '5'and strng[i] != '6'and strng[i] != '7'and strng[i] != '8'and strng[i] != '9':
            break
    if i == -1:
        new_num = 1
        return strng[-len(strng):] + str(new_num).zfill(len(strng[i:]))
    else:
        new_num = int(strng[i+1:]) + 1
        return strng[-len(strng):i+1] + str(new_num).zfill(len(strng[i+1:]))
print(increment_string('710'))























