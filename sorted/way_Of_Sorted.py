# _*_ coding: utf-8 _*_
# @Time     :2018/3/13 12:46
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""


def bubble_sort(arr):
    """
    冒泡排序终极改进版
    :param arr:
    :return:
    """
    n = len(arr)
    k = n
    for i in range(n - 1):
        flag = 1
        for j in range(k - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 0
                k = j + 1
        if flag:
            break
    return arr


def merge_sort(arr):
    """
    归并排序
    :param arr:
    :return:
    """
    n = len(arr)
    mid = n // 2
    if n <= 1:
        return arr
    larr = merge_sort(arr[:mid])
    rarr = merge_sort(arr[mid:])

    lpoint = 0
    rpoint = 0
    result = []

    while lpoint < len(larr) and rpoint < len(rarr):
        if larr[lpoint] <= rarr[rpoint]:
            result.append(larr[lpoint])
            lpoint += 1
        else:
            result.append(rarr[rpoint])
            rpoint += 1
    result += larr[lpoint:]
    result += rarr[rpoint:]
    return result


def quick_sort(arr, first, last):
    """
    快排
    :param arr:
    :return:
    """
    if first >= last:
        return
    mid_value = arr[first]
    low_point = first
    high_point = last

    while low_point < high_point:
        while low_point < high_point and arr[high_point] >= mid_value:
            high_point -= 1
        arr[low_point] = arr[high_point]

        while low_point < high_point and arr[low_point] < mid_value:
            low_point += 1
        arr[high_point] = arr[low_point]

        arr[low_point] = mid_value

        quick_sort(arr, first, low_point - 1)
        quick_sort(arr, low_point + 1, last)


if __name__ == '__main__':
    from random import randint

    a = [randint(0, 100) for _ in range(10)]
    print('*' * 20 + '原始列表如下' + '*' * 20)
    print(a)

    print('*' * 20 + '冒泡如下' + '*' * 20)
    print(bubble_sort(a))

    print('*' * 20 + '归并如下' + '*' * 20)
    newArr = merge_sort(a)
    print(newArr)

    print('*' * 20 + '快排如下' + '*' * 20)
    quick_sort(a, 0, len(a) - 1)
    print(a)
