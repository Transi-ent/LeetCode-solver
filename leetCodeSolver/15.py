"""
给定一个整型数组，找出所有的3元组，使元组和为0
"""

def threeSum(nums: list, target: int):

    d = dict()

    for i in range(len(nums)-1):

        for j in range(i, len(nums)):

            complement = -(nums[i]+nums[j])

            if d.get(complement):
                return [complement, nums[i], nums[j]]


            d[complement] = 1


