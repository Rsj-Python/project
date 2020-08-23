def pig_it(text):
    # 先将单词以空格分离保存在l1列表中
    l1 = text.split()
    l2 = []
    end_list = []
    # 将每个单词也弄成列表，便于操作
    for i in range(len(l1)):
        l2.append(list(l1[i]))
    # 对l2进行操作，先做将第一个字母移到后面的操作，并把结果保存到end_list列表中
    for i in range(len(l2)):
        l2[i].append(l2[i][0])
        l2[i].pop(0)
        a = ''.join(l2[i])
        end_list.append(a)
    # 对end_list列表中的元素加上ay，函数内会判断
    for i in range(len(end_list)):
        # 只给每个单词加上后缀ay，！和？标点符号不考虑，做一个判断
        if end_list[i] != '!' and end_list[i] != '?':
            end_list[i] = end_list[i] + 'ay'
    return ' '.join(end_list)
print(pig_it('Pig latin is cool ?'))





