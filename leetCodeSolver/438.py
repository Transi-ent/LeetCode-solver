# Find all anagrams in a string,
# 给定一个字符串s和一个非空字符串p，在S中找出所有P的anagrams子串，并返回这些子串的起始索引
from collections import Counter

def findAllAnagrams(s: str, p:str):
    # 固定长度的滑动窗口

    l, res, n, np = 0, [], len(s), len(p)

    freq = Counter(s[:np])

    dp = Counter(p)

    while l+np-1<n:

        # 判断滑动串口内的词频是否与字符串P的词频相同
        if freq==dp:
            res.append(l)

        freq[s[l]]-=1
        l+=1

    return res

