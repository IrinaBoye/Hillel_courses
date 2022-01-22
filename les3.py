list = [1, 8, 2, 3, 55, 22, 11, 1032, 22, 11]
new_list = []

while list:
    minimum = list[0]
    for number in list:
        if number < minimum:
            minimum = number
    new_list.append(minimum)
    list.remove(minimum)

print(new_list)

