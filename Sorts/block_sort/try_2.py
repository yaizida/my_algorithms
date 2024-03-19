def merge(a, b):
    idx1, idx2 = 0, 0
    res = []
    while idx1 < len(a) and idx2 < len(b):
        if a[idx1] >= b[idx2]:
            res.append(b[idx2])
            idx2 += 1
        else:
            res.append(a[idx1])
            idx1 += 1
    res += a[idx1:] + b[idx2:]
    return res


def sort(l, r):
    if r - l == 1:
        return [main[l]]
    mddl = (r + l) // 2
    l1 = sort(l, mddl)
    l2 = sort(mddl, r)
    return merge(l1, l2)


n = int(input())

if n == 0:
    raise SystemExit
main = list(map(int, input().split()))
print(*sort(0, len(main)))
