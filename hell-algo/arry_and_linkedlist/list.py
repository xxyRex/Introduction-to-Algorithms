# === File: list.py === """ 初始化列表 """
# 无初始值
list1 = []
# 有初始值 list2=[1,3,2,5,4]
list2 = [1, 3, 2, 5, 4]

""" 访问元素 """
num = list2[1]  # 访问索引 1 处的元素

""" 更新元素 """
list2[1] = 0  # 将索引 1 处的元素更新为 0

""" 清空列表 """
list2.clear()

""" 尾部添加元素 """
list2.append(1)
list2.append(3)
list2.append(2)
list2.append(5)
list2.append(4)

""" 中间插入元素 """
list2.insert(3, 6)  # 在索引 3 处插入数字 6

""" 删除元素 """
list2.pop(3)  # 删除索引 3 处的元素

""" 拼接两个列表 """
list1 = [6, 7, 8, 9, 10]
list2 += list1

""" 排序列表 """
list2.sort()  # 排序后，列表元素从小到大排列
