import itertools
# 1.(无限迭代器）这些用的不是很多，容易造成死循环
# count() cycle() repeat()



# 2.(排列组合迭代器)比较常用
# product()笛卡尔积
# for i in itertools.product('ab','cd'):
#     print(i,' ',end='')
# permutations(序列,所要输出值得个数) 所有可能的排序，不包含重复
print(list(itertools.permutations([2, 7, 11, 15],2)))
#combinations()按排序顺序，无重复元素
#combinations_with_replacement()  按排序顺序，带有重复的元素








