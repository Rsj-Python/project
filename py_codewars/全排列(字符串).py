def permutations(string):
    if len(string) <= 1:
        return string
    else:
        result = []
        for i in range(len(string)):
            for j in permutations(string[0:i] + string[i + 1:]):
                result.append(string[i] + j)
        return set(result)
print(permutations('abc'))


























