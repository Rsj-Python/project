def count_smileys(arr):
    count_num = 0
    eyes = [':',';']
    nose = ['','-','~']
    mouse = [')','D']
    for i in eyes:
        for j in nose:
            for k in mouse:
                face = i + j + k
                count_num += arr.count(face)
    return count_num
print(count_smileys([':D',':~)',';~D',':)']))

























