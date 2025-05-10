# class User:
#
#     age = 0;
#
#     def __init__(self, name):
#         print("я создался")
#         self.username = name
#
#     def sayName(self):
#         print("меня зовут", self.username)
#
#     def sayAge(self):
#         print(self.age)
#
#     def setAge(self, newAge):
#         self.age = newAge
#
#     def addCard(self, card):
#         self.card = card
#
#     def getCard(self, card):
#         return self.card

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")


