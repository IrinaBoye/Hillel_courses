elements = {"Au": "Золото", "Fe": "Железо", "H": "Водород"}

for key in elements.keys():
    print(key)

for value in elements.values():
    print(value)

elements ["O"] = "Кислород"
print(elements)

elements.pop("Fe")
print(elements)

for key, value in elements.items():
    print(key, value)

elements2 = elements.copy()
print(elements2)

elements2.clear()
print(elements2)
print(elements)

elements.update({"first": [1, 2, 3], "second": [4, 5]})
print(elements)

elements["first"] = [6, 7]
print(elements["first"])
print(elements)














