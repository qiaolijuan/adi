'''
练习：扑克牌，取红方色13张，用数字1-13来表示。13张牌从小到大排序后，将牌反面朝上，查找红方9
'''
# 二分查找法
# 每次查找的左侧下标值 left
# 每次查找的右侧下标值 right

def binary(value,key,left,right):
    # 递归退出的条件
    if left > right:
        # 查找失败返回-1
        return -1
    # 获取中间元素对应下标值
    middle = (left + right) // 2
    # 对比中间元素值与指定查找值
    if value[middle] == key:
        return middle # 查找成功返回对应下标值
    # 如果指定值小于中间值,则在左侧继续查找；查找范围减半，左侧下标值不变，右侧下标为中间值下标-1
    elif value[middle] > key:
        return binary(value,key,left,middle-1)
    # 如果指定值大于中间值，则在右侧继续查找；查找范围减半，右侧下标值不变，左侧下标为中间值下标+1
    else:
        return binary(value,key,middle+1,right)

if __name__ == "__main__":
    value = [1,2,3,4,5,6,7,8,9,10,11,12]
    key = 9
    left = value[0]
    right = len(value)-1
    res = binary(value,key,left,right)
    if res == -1:
        print("查找失败")
    else:
        print("红方9的下标是：",res)