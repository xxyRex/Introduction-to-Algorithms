# === File: array.py ===
""" 初始化数组 """
import random
from typing import List

arr = [0] * 5  # [0, 0, 0, 0]
nums = [1, 3, 2, 5, 4]


def random_access(nums: List[int]) -> int:
    """ 随机访问元素 """
    # 在区间 [0, len(nums)-1] 中随机抽取一个数字
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num


def extend(nums, enlarge):
    """ 扩展数组长度 """
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将原数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    return res


def insert(nums, num, index):
    """ 在数组的索引 index 处插入元素 num """
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(num) - 1, index, -1):
        nums[i] = nums[i - 1]
        # 将 num 赋给 index 处元素
        nums[index] = num


def remove(nums, index):
    """ 删除索引 index 处元素 """
    # 把索引 index 之后的所有元素向前移动一位
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]


def traverse(nums):
    """ 遍历数组 """
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count += 1
    # 直接遍历数组
    for num in nums:
        count += 1


def find(nums, target):
    """ 在数组中查找指定元素 """
    for i in range(len(nums)):
        if nums[i] == target:
            return i

        return -1
