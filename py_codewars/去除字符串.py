def clear_str(List):
    for i in List.copy():
        if type(i) == str:
            List.remove(i)
    return List
print(clear_str([1,2,'123','a',4,5]))



































