def narcissistic( value ):
    new_value = value
    list1 = []
    end_sum = 0
    for i in range(len(str(new_value))):
        list1.append(new_value % 10)
        new_value = new_value // 10
    for i in list1:
        end_sum += i**(len(list1))
    if end_sum == value:
        return True
    else:
        return  False

print(narcissistic(10))








