# 顺序查找
'''
练习：扑克牌，只取桃花色13张，用数字1-13来表示。洗牌后，将牌反面朝上排成一排，找到红桃6
'''

def linear(value,key):
    # 使用下标遍历所有数据
    for i in range(len(value)):
        # 对比当前获取数据与待查找值
        if value[i] == key:
            # 查找成功，返回对应下标值
            return i 
    # 遍历所有数据仍未找到时
    else:
        # 查找失败，返回-1
        return -1

if __name__ == "__main__":
    # 原始数据
    value = [3,2,5,4,6,7,9,8,10,11,13,12,1]
    key = 6

    # 顺序查找
    res = linear(value,key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功对应下标值：",res)
        