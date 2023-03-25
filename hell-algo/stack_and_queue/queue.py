"""
File: queue.py
Created Time: 2023-3-26
Author: xxyRex (xxy6459@gmail.com)
"""
import collections
from typing import Deque

if __name__ == "main":
    """ 初始化队列 """
    # 在 Python 中，我们一般将双向队列类 deque 看作队列使用
    # 虽然 queue.Queue() 是纯正的队列类，但不太好用
    que: Deque[int] = collections.deque()

    """ 元素入队 """
    que.append(1)
    que.append(2)
    que.append(3)
    que.append(5)
    que.append(4)
    print(f'队列 que ={que}')

    """ 访问队首元素 """
    front = que[0];

    """ 元素出队 """
    pop = que.popleft()

    """ 获取队列的长度 """
    size = len(que)

    """ 判断队列是否为空 """
    is_empty = len(que) == 0


























