def cakes(recipe, available):
    list1 = []
    for i in recipe.keys():
        if i not in available:
            return 0
            break
        else:
            list1.append(available[i] // recipe[i])
    return min(list1)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe,available))








































