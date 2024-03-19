import sys


def findLongestSubstring():
    s = sys.stdin.readline().rstrip()
    ma = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            tmp = s[i:j+1]
            if s[j] in tmp[:-1]:
                break
            ma = max(ma, tmp, key=len)
    return len(ma)


print(findLongestSubstring())
