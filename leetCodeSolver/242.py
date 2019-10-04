# 判断两个字符串是否互为Anagram
#
from collections import Counter

def validAnagram(s1: str, s2: str):

    if len(s1)!=len(s2):
        return False

    d = Counter(s1)

    for ch in s2:

        if d.get(ch):
            d[ch]-=1

        else:
            return False

        if d[ch]==0:
            del d[ch]

    return len(d)==0
