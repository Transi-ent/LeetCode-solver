# longest substring without repeating characters
# 给定一个字符串，找出这个字符串中最长的无重复元素的最长子串

def longestSubstring(s: str):

    l, r, res = 0, -1, 0 # 滑动窗口，[l ... r], 初始时，滑动窗口内的元素个数需为空

    freq = [0]*256 # 记录出现在滑动窗口中出现的所有字符的频率, ASCII取值在0~255

    while l<len(s):

        if r+1<len(s) and freq[ ord(s[r+1]) ]==0:
            # 滑动窗口右边界未触底，且右边界上的字母在频率表上显示为0
            r+=1
            freq[ord(s[r])]+=1

        else:
            freq[ord(s[l])]-=1
            l-=1

        res = max(res, r+1-l)

    return res
