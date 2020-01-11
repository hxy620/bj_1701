# 导包
import threading


# 定义唱歌
def sing(name):
    print("{}喜欢唱歌".format(name))


# 定义我是王
def king(name):
    print("我是王!")


# 实例化
t1 = threading.Thread(target=sing, args=("小曹",))
t2 = threading.Thread(target=king, args=("hxy",))
# 运行
t1.start()
t2.start()














