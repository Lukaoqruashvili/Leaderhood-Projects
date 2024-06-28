def divisible_by(numbers, divisor):
    lst = []
    for i in numbers:
        if i % divisor == 0:
            lst.append(i)
    return lst