def parts_sums(ls):
    lst = sum(ls)
    lst2 = [lst]
    for i in ls:
        lst = lst - i
        lst2.append(lst)
    return lst2