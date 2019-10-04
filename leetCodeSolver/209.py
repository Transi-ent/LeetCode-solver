# 给定一个数组，找出这个数组中最短连续子数组使得该子数组的和大于s

def minSubarrayLen(nums, target):

    left, right, n, res = 0, 0, len(nums), -1   # [left ... right] to store the sum of subarray

    sums = [nums[0]]*n

    for i in range(1, n):
        sums[i] = sums[i-1]+nums[i]

    while right<n:

        if (left==0 and sums[right]<target) or (sums[right]-sums[left-1]<target):

            right+=1

        else:
            if right+1-left<res:
                res=right+1-left

            left+=1

    return res


def minSubarrayLen2(nums, target):

    l, r, res, sum = 0, -1, -1, float('-inf')

    while l<len(nums):

        if r+1<len(nums) and sum<target:
            r +=1
            sum+=nums[r]


        else:
            sum -=nums[l]
            l+=1

        if sum>=target:
            res = min(res, r+1-l)

    return res







nums = [1,2,3,7,5]
rs = minSubarrayLen(nums, 6)
print(rs)

