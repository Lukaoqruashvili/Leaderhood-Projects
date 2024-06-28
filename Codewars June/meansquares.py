def solution(array_a, array_b):
    return sum([(y - x) ** 2 for x, y in zip(array_a, array_b)]) / len(array_a)