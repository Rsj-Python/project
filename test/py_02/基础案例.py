# 猜拳 石头剪刀布
# 任何电脑 人赢了几局 电脑赢了几局 一共进行了多少局

#倒入模块
import random
# 一共几局对战pk_sum 人赢了多少ren_win 电脑赢了多少com_win
pk_sum = 0
ren_win = 0
com_win = 0


# 选择对手
def selectHero():
    print('='*20+'欢迎来到曲阜师范第一届人机大战'+'='*20)
    #1.获取控制台，输入昵称
    global name
    name = input('请输入昵称:')
    #3.判断电脑序列号
    while True:
        # 2.获取控制台，输入电脑对战号
        hero = input('请输入你要对战的英雄\n1.钢铁侠\n2.雷神\n3.绿巨人:')
        global hero_name
        if hero == '1':
            hero_name = '钢铁侠'
            print('你选择的英雄是钢铁侠')
            print('=' * 68)
            break
        elif hero == '2':
            hero_name = '雷神'
            print('你选择的英雄是雷神')
            print('=' * 68)
            break
        elif hero == '3':
            hero_name = '绿巨人'
            print('你选择的英雄是绿巨人')
            print('=' * 68)
            break
        else:
            print('没有该英雄，请重新输入')
            print('='*68)

#开始PK
def ren_com_pk():
    global pk_sum
    global ren_win
    global com_win
    #循环对决
    while True:
        #统计PK次数
        pk_sum += 1
        #玩家的选择
        #输入序列号
        ren_key = int(input('请输入你的选择\n1.石头\n2.剪刀\n3.布:'))
        #根据序列号进行输出
        if ren_key == 1:
            print('你出了石头')
        elif ren_key == 2:
            print('你出了剪刀')
        elif ren_key == 3:
            print('你出了布')
        else:
            print('没有这个选项，重新选择')
            continue
        #电脑的选择
        #随机选择 randint():随机整数
        com_key = random.randint(1,3)
        #根据随机数字来决定电脑的出拳手势
        if com_key == 1:
            print('电脑选择了石头')
        elif com_key == 2:
            print('电脑选择了剪刀')
        else :
            print('电脑选择了布')
        #3.判断输赢
        #1.玩家赢
        if (ren_key == 1 and com_key == 2) or (ren_key == 2 and com_key ==3) or(ren_key == 3 and com_key == 1):
            print('你赢了，厉害了我的哥')
            print('=' * 68)
            ren_win += 1
        elif ren_key == com_key:
            print('平局，不服再战')
            print('=' * 68)
        #电脑赢
        else:
            print('电脑赢了，你真菜')
            print('=' * 68)
            com_win += 1
        #判断，5局比赛，胜场多的一方获胜
        if pk_sum >= 5:
            print('游戏结束')
            print('=' * 68)
            break
    print(f'{name}一共和{hero_name}进行了{pk_sum}场游戏\n你赢了{ren_win}局\n{hero_name}赢了{com_win}局\n最终结果为:')
    if ren_win > com_win:
        print('你取得了最后的胜利，厉害了，牛逼')
    elif ren_win == com_win:
        print('竟然平局了，不要走，再战')
    else:
        print('你输了，太菜了吧你，垃圾，连电脑都打不过')
        print('=' * 68)

# 结束游戏
def exits():
    global pk_sum
    global ren_win
    global com_win
    key = input('是否继续？输入no结束，输入yes继续:')
    if key == 'no':
        print('='*30+'游戏结束'+'='*30)
        exit()
    else:
        print('='*30+'继续游戏'+'='*31)
        # 初始化
        pk_sum = 0
        ren_win = 0
        com_win = 0
        ren_com_pk()
        exits()
# python程序入口
if __name__ == '__main__':
    selectHero()
    ren_com_pk()
    exits()




