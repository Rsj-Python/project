import easygui as ea
import sys
while 1:
    ea.msgbox('嗨，欢迎进入第一个界面小游戏')
    msg = '请问你希望在任陈村学到什么知识呢？'
    title = '任陈村欢迎您！'
    choices = ['种地','编程','国家公务员','考研']
    choice = ea.choicebox(msg,title,choices)
    ea.msgbox('你的选择是：' + str(choice),'结果')
    msg = '你希望重新进入人陈村吗？'
    title = '请选择'
    if ea.ccbox(msg,title):
        pass
    else:
        sys.exit(0)



