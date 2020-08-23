# 创建一个函数，用来求最终公交车上剩下的人数
def number(bus_stops):
    up_num = 0
    down_num = 0
    end_number = 0
    for i in range(len(bus_stops)):
        # 统计上车的人数
        up_num += bus_stops[i][0]
        # 统计下车的人数
        down_num += bus_stops[i][1]
    return up_num - down_num
print(number([[10,0],[3,5],[5,8]]))












