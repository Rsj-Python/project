def comp(array1,array2):
    try:
        return sorted(map(lambda i:i**2,array1)) == sorted(array2)
    except:
        return False
a = None
b = [1,2,3]
print(comp(a,b))

