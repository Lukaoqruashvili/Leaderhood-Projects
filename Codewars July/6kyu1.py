#Unique In Order
def unique_in_order(sequence):
    lst = []
    for i in sequence:
        if len(lst) == 0 or i != lst[-1]:
            lst.append(i)
    return lst  