def min_sum(arr):
    arr = sorted(arr)
    return sum(n*arr.pop() for n in arr)