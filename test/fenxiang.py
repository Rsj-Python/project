# ***员工管理系统***

# 打印一条欢迎使用语句
print('*'*20,'欢迎使用员工管理系统','*'*20)
# 下面需要写的是员工管理系统的功能
Emps = ['李务太\t 20\t 男\t淄博','任少杰\t 20\t 男\t禹城','赵文靓\t 28\t 女\t青岛']
while True:
    # 先让用户选择操作，给出用户可以进行的操作
    print('请输入您想要进行的操作：')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    # 创建一个变量接收用户输入的操作
    user_choose = input('请输入[1-4]：')
    print('*'*61)
    # 根据用户输入的不同分情况讨论1

    if user_choose == '1':
        # 查询员工输出结果为全部员工
        print('\t序号\t 姓名\t年龄\t性别\t住址')
        n = 1
        for Emp in Emps:
            print(f'\t {n}\t{Emp}')
            n += 1
        print('*'*61)
    elif user_choose == '2':
        # 增加员工
        emps_name = input('请输入你要添加的员工的姓名：')
        emps_age = input('请输入你要添加的员工的年龄：')
        emps_gender = input('请输入你要添加的员工的性别：')
        emps_address = input('请输入你要添加的员工的住址：')
        emps = f'{emps_name}\t {emps_age}\t {emps_gender}\t{emps_address}'
        print()
        # 显示输入的员工信息
        print('系统会将以下员工添加到员工库中')
        print(' 姓名\t年龄\t性别\t住址')
        print(emps)
        print('*'*61)
        user_decide = input('是否确认该操作？（请输入Yes或者No）')
        if user_decide == 'Yes':
            Emps.append(emps)
            print('添加成功！')
        elif user_decide == 'No':
            print('添加已取消！')
        else:
            print()
            print('你的输入有误，添加操作被迫取消！请重新选择你的操作')
        print()
        input('点击回车键继续！')
        print('*'*61)
    elif user_choose == '3':
        # 删除员工
        user_chooses = int(input('请输入你想要删除的员工序号：'))
        if  user_chooses > 0 and user_chooses <= len(Emps):
            # 显示要删除的员工信息
            print('以下员工将会被删除！')
            print('\t序号\t 姓名\t年龄\t性别\t住址')
            print(f'\t {user_chooses}\t{Emps[user_chooses-1]}')
            print('*'*61)
            user_decides = input('确定删除？（请输入Yes或者No）')
            # 判定用户输入
            if user_decides == 'Yes' :
                Emps.pop(user_chooses-1)
                print('删除成功！')
            elif user_decides == 'No':
                print('删除操作已取消！')
            else:
                print()
                print('你的输入有误，删除操作被迫取消！请重新选择你的操作！')
            print()
            input('点击回车键继续！')
        else:
            print(f'员工库中没有序号为{user_chooses}的员工，请重新进行删除操作！')
        print('*'*62)
    elif user_choose == '4':
        print('欢迎使用本系统！期待和您的再一次相见！')
        input('敲击回车键退出系统！')
        break
    else:
        print()
        print('你的输入有误！请重新输入！')
        input('点击回车键继续！')
        print('*'*61)

