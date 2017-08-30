import math
import random

def select(arr, k):
    n = len(arr)
    if len(arr) <= 10:
        if k <= n:
            return sorted(arr)[k - 1]
        else:
            return sorted(arr)[-1]

    partitions = []
    n = len(arr)
    for i in xrange(int(math.ceil(float(n) / 5))):
        s = i * 5
        e = s + 5
        partitions.append(arr[s:e])

    x = []
    for p in partitions:
        x.append(select(p, 3))

    M = select(x, n / 10)

    less = []
    equal = []
    more = []
    for val in arr:
        if val < M:
            less.append(val)
        elif val == M:
            equal.append(val)
        else:
            more.append(val)

    if k <= len(less):
        return select(less, k)
    elif k > len(less) + len(equal):
        return select(more, k - len(less) - len(equal))
    else:
        return M

if __name__ == "__main__":
    x = range(5000)
    random.shuffle(x)

    for i in xrange(1, len(x)):
        # assert select(x, i) == i - 1
        assert sorted(x)[i - 1] == i - 1
