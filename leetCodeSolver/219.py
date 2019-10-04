"""
给定一个整形数组nums 和一个整数 k, 是否存在索引i 和 j,
使得 nums[i]==nums[j]，且i, j 之差不大于k
"""

def containDuplicate(nums: list, k):

    l, r = 0, -1 # [l ... r] 滑动窗口范围

    s = set()

    while r<len(nums):

        if r+1<len(nums) and r+1-l<k:
            r+=1
            tmp = nums[r]
            if s.__contains__(tmp):
                return True

            s.add(tmp)

        else:
            s.remove(nums[l])
            l+=1

    return False




