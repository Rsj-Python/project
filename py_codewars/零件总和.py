def parts_sums(ls):
    result = [sum(ls)]
    # for item in ls:
    #     result.append(result[-1] - item)
    return result
print(parts_sums([0, 1, 3, 6, 10]))