# _*_ coding: utf-8 _*_
# @Time     :2018/3/13 12:46
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""


def binary_search(arr, item):
    """
    二分查找，递归版本
    :param arr:
    :param item:
    :return:
    """
    n = len(arr)
    if n > 0:
        mid_point = n // 2
        if arr[mid_point] == item:
            print('找到了')
            return item
        elif item < arr[mid_point]:
            return binary_search(arr[:mid_point], item)
        else:
            return binary_search(arr[mid_point:], item)
    print('没找到')
    return False


def binary_search2(arr, item):
    """
    二分查找，非递归版本
    :param arr:
    :param item:
    :return:
    """
    n = len(arr)
    first_point = 0
    last_point = n - 1
    while first_point <= last_point:
        mid_point = (first_point + last_point) // 2
        if arr[mid_point] == item:
            print('找到了')
            return item
        elif item < arr[mid_point]:
            last_point = mid_point - 1
        else:
            first_point = mid_point + 1
    print('找到了')
    return False


if __name__ == "__main__":
    a = [11, 27, 27, 63, 67, 73, 74, 86, 98, 100]

    b = binary_search(a, 11)
    print(b)

    b = binary_search2(a, 11)
    print(b)
