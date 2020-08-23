
import csv

# writer方法
# 可接收一个文件对象和一个分隔符。并返回一个带writerow方法的CSV对象。
with open("jie.csv","w") as file_obj:
    w = csv.writer(file_obj,delimiter=",",lineterminator="\n")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])

# reader方法，传入文件对象并以逗号作为分隔符，会返回一个可迭代的对象
with open("jie.csv","r") as file_obj:
    res = csv.reader(file_obj,delimiter=",")
    for re in res:
        print(','.join(re))