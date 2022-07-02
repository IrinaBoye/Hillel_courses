class Pizza:
    def __init__(self, name_of_pizza, size, price):
        self.name_of_pizza = name_of_pizza
        self.size = size
        self.price = price
        self.number_of_likes = 0

    def make_an_order(self, number_of_order):
        self.number_of_likes += number_of_order

    def __str__(self):
        return f"{self.name_of_pizza}, {self.size}, {self.price}"


class Cook:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.experience = 0

    def cooking(self, number_of_pizza):
        self.experience += number_of_pizza

    def __str__(self):
        return f"{self.name}"


pizza_1 = Pizza('Pepperoni', 40, 200)
pizza_2 = Pizza('Quattro Formaggi', 30, 150)
print(pizza_1)
print(pizza_2)
pizza_1.make_an_order(3)
print(pizza_1.number_of_likes)
pizza_2.make_an_order(10)
print(pizza_2.number_of_likes)
cook_1 = Cook('Jon', 25)
cook_2 = Cook('Bob', 37)
print(cook_1)
print(cook_2)
cook_1.cooking(4)
print(cook_1.experience)
cook_2.cooking(9)
print(cook_2.experience)







