list1 = [1, 22812, 9, 7, 653, 0]


def largest_number(a):
    if all(v == 0 for v in a):
        return '0'
    return ''.join(sorted((str(v) for v in a), reverse=True))


print(largest_number(list1))
