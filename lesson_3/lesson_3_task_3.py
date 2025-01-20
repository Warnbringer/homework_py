# from user import User
# from card import Card
#
# Ader = User("Ader")
#
# Ader.sayName()
#
# Ader.sayAge()
# Ader.setAge(56)
# Ader.sayAge()
#
#
# Ader.addCard(Card)
# Ader.getCard().pay(1000)
#
# card = Card("2345 5677 8799 4536", "11/26", "Ader F")

from user import User

my_user = User("Роман", "Павлов")

my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()



from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234337"),
    Smartphone("Samsung", "Galaxy S22", "+79007334321"),
    Smartphone("Xiaomi", "Mi 11", "+79009336543"),
    Smartphone("Google", "Pixel 6", "+79003453389"),
    Smartphone("OnePlus", "9 Pro", "+79004567330"),]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")



from address import Address
from mailing import Mailing

# Создание экземпляров класса Address
to_address = Address("123999", "Омск", "Рубцова", "4", "8")
from_address = Address("654888", "Саратов", "Березовая", "56", "123")

# Создание экземпляра класса Mailing
mailing = Mailing(to_address, from_address, 350, "TRK123456")

# Печать информации об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")