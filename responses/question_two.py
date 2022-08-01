def max_sums(values: list):
    return sum(sorted(values, reverse=True)[0:2])


assert max_sums([1, 10, 3, 7, 9]) == 19
assert max_sums([-2, 1, -1, 0]) == 1
assert max_sums([3, 9, 2, 2, 8, 7, 5]) == 17
