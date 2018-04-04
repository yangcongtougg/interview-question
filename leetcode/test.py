# _*_ coding: utf-8 _*_
# @Time     :2018/3/27 10:14
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        temp = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                temp.append(nums1[0])
                del nums1[0]
            else:
                temp.append(nums2[0])
                del nums2[0]
        temp.extend(nums1)
        temp.extend(nums2)

        point = len(temp) % 2
        if point == 0:
            return float((temp[(len(temp) // 2) - 1] + temp[len(temp) // 2]) / 2)
        else:
            return float(temp[len(temp) // 2])


if __name__ == '__main__':
    a = Solution()
    b = a.findMedianSortedArrays([1, 3], [2])
    print(b)
