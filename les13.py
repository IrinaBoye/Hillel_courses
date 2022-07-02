class Phone:
    model = str()
    weight = int()
    color = str()
    location = str()

    def __init__(self, number):
        self.number = number

    def call(self, number):
        print(f"Calling a phone number {number}")

    def send_sms(self, *numbers, text):
        print(f"Sms {text} was sent to {','.join(*numbers)}")

    def contact_list(self, *names, **numbers):
        pass

    def add_contact(self, name, number):
        pass

    def get_info(self):
        print(f"New phone {self.model} with number {self.number} (weight - {self.weight}, color - {self.color}, "
              f"location - {self.location}).")


class Xiaomi(Phone):
    model = "xiaomi"
    weight = 180
    color = "black"
    location = "en"


class Realme(Phone):
    model = "realme"
    weight = 190
    color = "white"
    location = "ru"


class Samsung(Phone):
    model = "samsung"
    weight = 200
    color = "red"
    location = "uk"


xiaomi_1 = Xiaomi(1111111)
xiaomi_2 = Xiaomi(1111112)
xiaomi_3 = Xiaomi(1111113)
xiaomi_4 = Xiaomi(1111114)
xiaomi_5 = Xiaomi(1111115)
xiaomi_1.get_info()
xiaomi_2.get_info()
xiaomi_3.get_info()
xiaomi_4.get_info()
xiaomi_5.get_info()

realme_1 = Realme(2111111)
realme_2 = Realme(2111112)
realme_3 = Realme(2111113)
realme_4 = Realme(2111114)
realme_5 = Realme(2111115)
realme_1.get_info()
realme_2.get_info()
realme_3.get_info()
realme_4.get_info()
realme_5.get_info()

samsung_1 = Samsung(3111111)
samsung_2 = Samsung(3111112)
samsung_3 = Samsung(3111113)
samsung_4 = Samsung(3111114)
samsung_5 = Samsung(3111115)
samsung_1.get_info()
samsung_2.get_info()
samsung_3.get_info()
samsung_4.get_info()
samsung_5.get_info()


