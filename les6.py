list1 = [1, 2, 55, 44, 33, 22, 11, 0, 123, 637, 123123]
list2 = []

for el in list1:
    if el == 637:
        break
    elif el % 2 == 1:
        list2.append(el)

print(list2)
