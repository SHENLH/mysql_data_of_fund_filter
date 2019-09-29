"""
util
~~~~
功能增强函数，多为通用函数
"""
from math import floor


def funds_split(funds_list, length=2000):
    """
    切分基金列表，由于Wind对单次提取的数据长度有限制，建议每次提取的基金数不超过2000个
    :param funds_list: 原始基金序列 :List
    :param length: 切分后单个列表长度 :int
    :return: 切分后的基金列表 :List<List<String>>
    """
    num = floor(len(funds_list)/length)
    funds_separated = []
    for i in range(num):
        separated = funds_list[length*i: length*(i+1)]
        funds_separated.append(separated)
    last = funds_list[length*num:]
    if last:
        funds_separated.append(last)
    return funds_separated
