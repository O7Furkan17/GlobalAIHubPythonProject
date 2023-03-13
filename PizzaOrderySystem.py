import csv
import datetime

menuu = "Please Choose a Pizza Base:  " \
        "\n1: Classic" \
        "\n2: Margherita" \
        "\n3: TurkPizza(lahmacun)" \
        "\n4: Pepperoni" \
        "\n5: Four Seasons Pizza" \
        "\n And sauce of your choice:  " \
        "\n1: Olives" \
        "\n2: Mushrooms" \
        "\n3: GoatCheese" \
        "\n4: Meat" \
        "\n5: Onions" \
        "\n6: Corn"
with open("menu.txt", 'w') as menu:
    menu.write(menuu)


class Pizza:
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Classic(Pizza):
    def get_description(self):
        return "Classic Pizza"

    def get_cost(self, size):
        return 7.25 + (size * 2)


class Margherita(Pizza):
    def get_description(self):
        return "Margherita Pizza"

    def get_cost(self, size):
        return 8.90 + (size * 2)


class Lahmacun(Pizza):
    def get_description(self):
        return "Turk Pizza (Lahmacun)"

    def get_cost(self, amount):
        return 3 * amount


class Pepperoni(Pizza):
    def get_description(self):
        return "Pepperoni Pizza"

    def get_cost(self, size):
        return 10 + (size * 2)


class FourSeasons(Pizza):
    def get_description(self):
        return "Four Seasons Pizza"

    def get_cost(self, size):
        return 10 + (size * 2)


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olives(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Olives"
        self.cost = 0.99

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.component.get_description() + ", " + self.description


class Mushrooms(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mushrooms"
        self.cost = 1.25

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.component.get_description() + ", " + self.description


class GoatCheese(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Goat Cheese"
        self.cost = 1.25

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.component.get_description() + ", " + self.description


class Meat(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Meat"
        self.cost = 1.99

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.component.get_description() + ", " + self.description


class Onions(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Onions"
        self.cost = 0.99

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.component.get_description() + ", " + self.description


class Corn(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Corn"
        self.cost = 0.99

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.component.get_description() + ", " + self.description


def get_pizza_choice():
    while True:
        print("Choose a pizza. İf you want to exit enter 'q' :")
        choice = input()
        if choice == "1":
            return Classic()
        elif choice == "2":
            return Margherita()
        elif choice == "3":
            return Lahmacun()
        elif choice == "4":
            return Pepperoni()
        elif choice == "5":
            return FourSeasons()
        elif choice == "q":
            return None
        else:
            print("Invalid choice!")


def get_size():
    choice = -1
    while choice == -1:
        print("Please choose size:\n"
              "0-Small\n"
              "1-Medium\n"
              "2-Large")
        try:
            choice = int(input())
        except:
            choice = -1
        if choice == 1 or choice == 2 or choice == 0:
            return choice
        else:
            print("İnvalid choice!")


def get_sauce_choice(pizza):
    choice = 0
    while True:
        print("1: Olives\n"
              "2: Mushrooms\n"
              "3: GoatCheese\n"
              "4: Meat\n"
              "5: Onions\n"
              "6: Corn")
        try:
            choice = int(input())
        except:
            pass
        if choice == 1:
            return Olives(pizza)
        elif choice == 2:
            return Mushrooms(pizza)
        elif choice == 3:
            return GoatCheese(pizza)
        elif choice == 4:
            return Meat(pizza)
        elif choice == 5:
            return Onions(pizza)
        elif choice == 6:
            return Corn(pizza)
        else:
            print("İnvalid selection")


def id_checker(id_number):
    if len(id_number) != 11 or not id_number.isdigit():
        print(id_number)
        print("Invalid ID number")
        return False
    else:
        return True


def get_last_credit_card(id_number):
    last_credit_card = ""
    try:
        with open("Orders_Database.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == id_number:
                    last_credit_card = row[2]
    except FileNotFoundError:
        pass
    return last_credit_card


def add_order_to_database(name, id_number, credit_card_number, pizza_description):
    with open("Orders_Database.csv", "a", newline="") as file:
        writer = csv.writer(file)
        now = datetime.datetime.now()
        order_time = now.strftime("%d-%m-%Y %H:%M:%S")
        writer.writerow([name, id_number, credit_card_number, pizza_description, order_time])


def credit_card_checker(credit_card):
    if len(credit_card) != 16 or not credit_card.isdigit():
        return False
    else:
        return True


if __name__ == '__main__':
    print(menuu)
    cost = 0.0
    pizza_choice = get_pizza_choice()
    if pizza_choice is not None:
        print(pizza_choice.get_description())
        c1 = input("Any sauce ?\nİf you want please enter '1'\n")
        if c1 == "1":
            souce = get_sauce_choice(pizza_choice)
            if pizza_choice.get_description() == "Turk Pizza (Lahmacun)":
                size = 0
                while size <= 0:
                    size = int(input("How many Turk Pizza do you want?\n"))
                    if size <= 0:
                        print("Invalid selection")
                cost = pizza_choice.get_cost(size) + souce.get_cost()
            else:
                size = get_size()
                cost = pizza_choice.get_cost(size) + souce.get_cost()
            if size == 0:
                size_text ="Small"
            elif size == 1:
                size_text ="Medium"
            else :
                size_text = "Large"

            description = souce.get_description() + ", " + size_text
            print(description)
            print("Cost : " + str(cost)+"$")

        else:
            size = get_size()
            if size == 0:
                size_text ="Small"
            elif size == 1:
                size_text ="Medium"
            else :
                size_text = "Large"
            cost = str(pizza_choice.get_cost(size))
            description = pizza_choice.get_description() + " ," + size_text
            print(description + " " + cost+"$")
        name = input("Name Surname :")
        id_number = input("Enter your ID number:\n")
        is_İd = id_checker(id_number)
        while True:
            if is_İd == False:
                id_number = input("Please check your ID number:\n")
                is_İd = id_checker(id_number)
            else:
                break

        last_credit_card = get_last_credit_card(id_number)

        if last_credit_card:
            use_last_credit_card = input("Do you want to use last credit card information? (Y/N): ")
            if use_last_credit_card.lower() == "y":
                credit_card_number = last_credit_card
            else:
                credit_card_number = input("Enter your credit card number: ")
                isCreditcard = credit_card_checker(credit_card_number)
                while True:
                    if not isCreditcard:
                        credit_card_number = input("Please check your Credit Card İnformation:\n")
                        isCreditcard = credit_card_checker(credit_card_number)
                    else:
                        break
        else:
            credit_card_number = input("Enter your credit card number: ")
            isCreditcard = credit_card_checker(credit_card_number)
            while True:
                if not isCreditcard:
                    credit_card_number = input("Please check your Credit Card İnformation:\n")
                    isCreditcard = credit_card_checker(credit_card_number)
                else:
                    break

        add_order_to_database(name, id_number, credit_card_number, description)

        print("Your order is taked, enjoy it :)")
    else:
        print("See you again ! ")
