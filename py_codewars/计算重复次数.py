def duplicate_count(text):
    new_text = text.lower()
    new_list = list(new_text)
    count = 0
    for str in new_list.copy():
        if new_list.count(str) >1 :
            for i in range(new_list.count(str)):
                new_list.remove(str)
            count += 1
    return count
print(duplicate_count("aAbcc"))






















