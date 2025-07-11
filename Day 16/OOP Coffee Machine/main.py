from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            print(moneyMachine.make_payment(drink.cost))