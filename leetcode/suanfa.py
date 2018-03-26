# _*_ coding: utf-8 _*_
# @Time     :2018/3/19 10:56
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""


# 给定nums = [2,7,11,15]，目标= 9，
#
# 由于nums [ 0 ] + nums [ 1 ] = 2 + 7 = 9，
# 返回[ 0，1 ]。
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


# 翻转
class Solution2(object):
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        max_int = 2147483647
        temp = abs(n)
        result = 0
        while temp > 0:
            result *= 10
            result += temp % 10
            if result > max_int:
                return 0
            temp = temp // 10
        return result if n >= 0 else -result


# 回文
class Solution3(object):
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True


def myleng(s):
    if s is None or len(s) == 0:
        return 0
    left = 0
    dic = {}
    temp = 0
    for i in range(len(s)):
        if s[i] in dic and dic[s[i]] >= left:
            left = dic[s[i]] + 1
        dic[s[i]] = i
        temp = max(temp, i - left + 1)
    return temp












if __name__ == '__main__':
    # from collections import Counter
    # a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # count = Counter(tuple(sorted(s))for s in a)
    # b = filter(lambda x:count[tuple(sorted(x))]>1,a)
    # print(list(b))
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    dic = {}
    for item in sorted(strs):
        sortedItem = ''.join(sorted(item))
        print(sortedItem)
        dic[sortedItem] = dic.get(sortedItem, []) + [item]
        print(dic[sortedItem])
    print(dic.values())













