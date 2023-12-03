class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing an action"

    def status(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee} g of coffee beans")
        print(f"{self.cups} disposable cups")
        print(f"${self.money} of money")

    def buy(self, option):
        if option == '1':
            self.make_coffee(250, 0, 16, 4)
        elif option == '2':
            self.make_coffee(350, 75, 20, 7)
        elif option == '3':
            self.make_coffee(200, 100, 12, 6)

    def fill(self, water, milk, coffee, cups):
        self.water += int(water)
        self.milk += int(milk)
        self.coffee += int(coffee)
        self.cups += int(cups)

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def make_coffee(self, water_needed, milk_needed, coffee_needed, cost):
        if self.water < water_needed:
            print("Sorry, not enough water!")
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
        elif self.coffee < coffee_needed:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee -= coffee_needed
            self.money += cost
            self.cups -= 1

    def input_handler(self, input_string):
        if self.state == "choosing an action":
            if input_string == "buy":
                self.state = "choosing a type of coffee"
            elif input_string == "fill":
                self.state = "asking for water"
            elif input_string == "take":
                self.take()
            elif input_string == "remaining":
                self.status()
            elif input_string == "exit":
                exit()
        elif self.state == "choosing a type of coffee":
            self.buy(input_string)
            self.state = "choosing an action"
        elif self.state == "asking for water":
            self.fill(input_string, 0, 0, 0)
            self.state = "asking for milk"
        elif self.state == "asking for milk":
            self.fill(0, input_string, 0, 0)
            self.state = "asking for coffee"
        elif self.state == "asking for coffee":
            self.fill(0, 0, input_string, 0)
            self.state = "asking for cups"
        elif self.state == "asking for cups":
            self.fill(0, 0, 0, input_string)
            self.state = "choosing an action"

def main():
    machine = CoffeeMachine()

    while True:
        if machine.state == "choosing an action":
            action = input("Write action (buy, fill, take, remaining, exit): ")
        elif machine.state == "choosing a type of coffee":
            action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        elif machine.state == "asking for water":
            action = input("Write how many ml of water you want to add: ")
        elif machine.state == "asking for milk":
            action = input("Write how many ml of milk you want to add: ")
        elif machine.state == "asking for coffee":
            action = input("Write how many grams of coffee beans you want to add: ")
        elif machine.state == "asking for cups":
            action = input("Write how many disposable cups you want to add: ")
        
        machine.input_handler(action)

if __name__ == "__main__":
    main()

