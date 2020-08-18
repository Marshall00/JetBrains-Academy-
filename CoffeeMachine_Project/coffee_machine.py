class Cofee_machine:

    water = 500
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.machine_action()

    def __str__(self):
        return("""
                The coffee machine has:
                %s of water
                %s of milk
                %s of coffee beans
                %s of disposable cups
                %s of money
                """ % (self.water, self.milk, self.beans, self.cups, self.money))

    def machine_action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            self.action = str(input())

            if self.action == 'buy':
                self.buy()
            elif self.action == 'fill':
                self.fill()
            elif self.action == 'take':
                self.take()
            elif self.action == 'remaining':
                self.remaining()
            elif self.action == 'exit':
                break

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:')
        self.coffee_type = str(input())

        if self.coffee_type != 'back':

            if self.coffee_type == '1':
                if self.water - 250 < 0:
                    print("Sorry, not enough water!")
                elif self.beans - 16 < 0:
                    print("Sorry, not enough coffee beans!")
                elif self.cups - 1 < 0:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                    self.cups -= 1

            elif self.coffee_type == '2':
                if self.water - 350 < 0:
                    print("Sorry, not enough water!")
                elif self.milk - 75 < 0:
                    print("Sorry, not enough milk!")
                elif self.beans - 20 < 0:
                    print("Sorry, not enough coffee beans!")
                elif self.cups - 1 < 0:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                    self.cups -= 1

            elif self.coffee_type == '3':
                if self.water - 200 < 0:
                    print("Sorry, not enough water!")
                elif self.milk - 100 < 0:
                    print("Sorry, not enough milk!")
                elif self.beans - 12 < 0:
                    print("Sorry, not enough coffee beans!")
                elif self.cups - 1 < 0:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                    self.cups -= 1

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water_fill = int(input())
        self.water += water_fill

        print('Write how many ml of milk do you want to add:')
        milk_fill = int(input())
        self.milk += milk_fill

        print('Write how many grams of coffee beans do you want to add:')
        beans_fill = int(input())
        self.beans += beans_fill

        print('Write how many disposable cups of coffee do you want to add:')
        cups_fill = int(input())
        self.cups += cups_fill

    def take(self):
        print('I gave you $%s' % self.money)
        self.money = 0

    def remaining(self):
        print(self.__str__())

Cofee_machine()